import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicVariable {
    // Reemplazamos 'int coins' por un AtomicInteger
    static AtomicInteger coins = new AtomicInteger(10000);
    private static final int CONSUMO = 1000;

    public static void consumirMonedas(String nombre) {
        // La operación de resta y actualización es atómica (segura)
        int nuevoValor = coins.addAndGet(-CONSUMO); 
        
        System.out.println(nombre + " -> Balance: " + nuevoValor);

        // Opcional: Simular el retraso fuera de una región sincronizada
        try { Thread.sleep(1); } catch (InterruptedException ignored) {}
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
        System.out.println("--- 3. Variables Atómicas ---");
        System.out.print("Introduce el número de jugadores: ");
        int numJugadores = scanner.nextInt();
        scanner.close();

        Thread[] hilos = new Thread[numJugadores];
        
        System.out.println("\nInicio: " + coins.get());
        
        for (int i = 0; i < numJugadores; i++) {
            hilos[i] = new JugadorThread("J-" + (i + 1));
            hilos[i].start(); 
        }
        
        for (Thread h : hilos) { h.join(); } 

        int esperado = 10000 - (numJugadores * CONSUMO);
        int finalReal = coins.get();
        
        System.out.println("\nFinal Calculado: " + esperado);
        System.out.println("Final Real: " + finalReal);
        System.out.println("Resultado: " + (finalReal == esperado ? "CORRECTO" : "INCORRECTO"));
    }
}