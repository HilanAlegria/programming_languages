import java.util.Scanner;

public class syncrhronized_method {
    // Recurso compartido
    static int coins = 10000;
    private static final int CONSUMO = 1000;

    // El método ESTÁTICO está sincronizado
    public static synchronized void consumirMonedas(String nombre) {
        // Sección Crítica protegida:
        int currentCoins = coins;
        try { Thread.sleep(1); } catch (InterruptedException ignored) {} // Simular trabajo
        coins = currentCoins - CONSUMO;
        
        System.out.println(nombre + " -> Balance: " + coins);
    }

    static class JugadorThread extends Thread {
        private final String nombre;
        public JugadorThread(String name) { this.nombre = name; }

        @Override
        public void run() {
            consumirMonedas(this.nombre);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("--- 1. Métodos Sincronizados ---");
        System.out.print("Introduce el número de jugadores: ");
        int numJugadores = scanner.nextInt();
        scanner.close(); // Se cierra aquí para evitar advertencias

        Thread[] hilos = new Thread[numJugadores];
        
        System.out.println("\nInicio: " + coins);
        
        for (int i = 0; i < numJugadores; i++) {
            hilos[i] = new JugadorThread("J-" + (i + 1));
            hilos[i].start(); // Crea un hilo por cada jugador
        }
        
        for (Thread h : hilos) { h.join(); } // Esperar a que todos terminen

        int esperado = 10000 - (numJugadores * CONSUMO);
        System.out.println("\nFinal Calculado: " + esperado);
        System.out.println("Final Real: " + coins);
        System.out.println("Resultado: " + (coins == esperado ? "CORRECTO" : "INCORRECTO"));
    }
}