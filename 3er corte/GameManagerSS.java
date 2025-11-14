import java.util.Scanner;

// La interfaz la cambiamos a una clase para poder implementar la lógica del programa
public class GameManagerSS {

    // Variable estática que corresponde al recurso compartido (sin sincronización)
    static int coins = 10000;
    
    // Cantidad de monedas que cada jugador intentará consumir
    private static final int CONSUMO_POR_JUGADOR = 1000;

    // Clase interna que define el comportamiento del hilo (cada jugador)
    static class PlayerThread extends Thread {
        private String playerName;
        
        public PlayerThread(String name) {
            this.playerName = name;
        }

        @Override
        public void run() {
            // *** Sección Crítica (sin sincronización) ***
            // La operación de leer, modificar y escribir no es atómica
            
            // 1. Leer el valor actual de coins
            int currentCoins = coins;
            
            // Simular un poco de trabajo o un retraso para aumentar la probabilidad del problema de carrera
            try {
                Thread.sleep(10); // Pausa mínima
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            // 2. Calcular el nuevo valor
            int newCoins = currentCoins - CONSUMO_POR_JUGADOR;

            // 3. Escribir el nuevo valor de vuelta al recurso compartido
            coins = newCoins;
            
            System.out.println(playerName + " consumió " + CONSUMO_POR_JUGADOR + 
                               " monedas. Balance temporal: " + newCoins);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. Pedir número de jugadores
        System.out.println("--- Simulación de Concurrencia (Sin Sincronización) ---");
        System.out.print("Introduce el número de jugadores (hilos): ");
        int numPlayers = 0;
        try {
            numPlayers = scanner.nextInt();
        } catch (java.util.InputMismatchException e) {
            System.out.println("Entrada inválida. Usando 5 jugadores por defecto.");
            numPlayers = 5;
        }
        scanner.close();
        
        System.out.println("\nBalance Inicial de Monedas: " + coins);
        System.out.println("Cada jugador consumirá: " + CONSUMO_POR_JUGADOR + " monedas.");
        System.out.println("---------------------------------------------------------");

        // 2. Crear un hilo por cada jugador
        Thread[] players = new Thread[numPlayers];
        for (int i = 0; i < numPlayers; i++) {
            players[i] = new PlayerThread("Jugador-" + (i + 1));
        }

        // Iniciar todos los hilos
        for (Thread player : players) {
            player.start();
        }

        // 3. Esperar a que todos los hilos terminen (Join)
        try {
            for (Thread player : players) {
                player.join(); // El hilo principal espera a que este hilo muera
            }
        } catch (InterruptedException e) {
            System.out.println("El hilo principal fue interrumpido.");
        }

        // 4. Al final debe imprimirse el balance final de monedas
        
        int expectedCoins = 10000 - (numPlayers * CONSUMO_POR_JUGADOR);
        
        System.out.println("\n=========================================================");
        System.out.println("Balance FINAL de Monedas (coins): " + coins);
        System.out.println("Balance ESPERADO (Correcto): " + expectedCoins);
        System.out.println("=========================================================");
        
        if (coins != expectedCoins) {
            System.err.println("¡ATENCIÓN! El balance final es INCORRECTO debido a una condición de carrera (Race Condition).");
        } else {
            System.out.println("El balance final es, por casualidad, correcto. Intenta ejecutarlo de nuevo.");
        }
    }
}