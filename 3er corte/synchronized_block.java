import java.util.Scanner;

public class synchronized_block {
    static int coins = 10000;
    private static final int CONSUMO = 1000;
    
    // Objeto de bloqueo estático dedicado
    private static final Object LOCK = new Object(); 

    public static void consumirMonedas(String nombre) {
        // Bloque Sincronizado: solo un hilo puede entrar a este bloque a la vez
        synchronized (LOCK) { 
            // Sección Crítica protegida:
            int currentCoins = coins;
            try { Thread.sleep(1); } catch (InterruptedException ignored) {}
            coins = currentCoins - CONSUMO;
            
            System.out.println(nombre + " -> Balance: " + coins);
        } // El bloqueo se libera automáticamente al salir del bloque
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
        System.out.println("--- 2. Bloques Intrínsecos ---");
        System.out.print("Introduce el número de jugadores: ");
        int numJugadores = scanner.nextInt();
        scanner.close();

        Thread[] hilos = new Thread[numJugadores];
        
        System.out.println("\nInicio: " + coins);
        
        for (int i = 0; i < numJugadores; i++) {
            hilos[i] = new JugadorThread("J-" + (i + 1));
            hilos[i].start(); 
        }
        
        for (Thread h : hilos) { h.join(); } 

        int esperado = 10000 - (numJugadores * CONSUMO);
        System.out.println("\nFinal Calculado: " + esperado);
        System.out.println("Final Real: " + coins);
        System.out.println("Resultado: " + (coins == esperado ? "CORRECTO" : "INCORRECTO"));
    }
}