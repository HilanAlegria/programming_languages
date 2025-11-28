import java.util.*;
import java.util.concurrent.locks.ReentrantLock;

public class SistemaRecompensas {

    // === Clase Jugador ===
    static class Jugador {
        private String nombre;
        private int monedas = 0;
        private List<String> inventario;
        
        // Lock para sincronizar acceso a monedas e inventario
        private final ReentrantLock lock = new ReentrantLock();

        public Jugador(String nombre) {
            this.nombre = nombre;
            this.inventario = new ArrayList<>();
        }

        // Método sincronizado usando Lock
        public void agregarMonedas(int cantidad) {
            lock.lock();
            try {
                monedas += cantidad;  // SECCIÓN CRÍTICA
            } finally {
                lock.unlock();
            }
        }

        public void agregarItem(String item) {
            lock.lock();
            try {
                inventario.add(item);  // SECCIÓN CRÍTICA
            } finally {
                lock.unlock();
            }
        }

        public int getMonedas() {
            return monedas;
        }

        public List<String> getInventario() {
            return inventario;
        }

        // Getter para nombre para evitar advertencia de campo no usado
        public String getNombre() {
            return nombre;
        }
    }

    // === Clase Mision (Runnable) ===
    static class Mision implements Runnable {
        private Jugador jugador;
        private static final String[] ITEMS = {"Espada", "Poción", "Escudo"};

        public Mision(Jugador jugador) {
            this.jugador = jugador;
        }

        @Override
        public void run() {
            Random random = new Random();

            // Recompensas
            int monedasGanadas = random.nextInt(100) + 1;
            String item = ITEMS[random.nextInt(ITEMS.length)];

            // Actualizando recursos del jugador
            jugador.agregarMonedas(monedasGanadas);
            jugador.agregarItem(item);

            System.out.println(Thread.currentThread().getName() +
                    " completó misión → +" + monedasGanadas + " monedas, item: " + item);
        }
    }

    // === MAIN ===
    public static void main(String[] args) throws InterruptedException {

        Jugador jugador = new Jugador("Héroe");

        // Crear 3 misiones concurrentes
        Thread m1 = new Thread(new Mision(jugador), "Mision-1");
        Thread m2 = new Thread(new Mision(jugador), "Mision-2");
        Thread m3 = new Thread(new Mision(jugador), "Mision-3");

        // Iniciar hilos
        m1.start();
        m2.start();
        m3.start();

        // Mostrar resultados
        System.out.println("\n===== ESTADO FINAL DEL JUGADOR =====");
        System.out.println("Jugador: " + jugador.getNombre());
        System.out.println("Monedas totales: " + jugador.getMonedas());
        System.out.println("Inventario: " + jugador.getInventario());
        System.out.println("====================================");
        // Mostrar resultados
        System.out.println("\n===== ESTADO FINAL DEL JUGADOR =====");
        System.out.println("Jugador: " + jugador.getNombre());
        System.out.println("Monedas totales: " + jugador.getMonedas());
        System.out.println("Inventario: " + jugador.getInventario());
        System.out.println("====================================");

        System.out.println("\n===== ESTADO FINAL DEL JUGADOR =====");
        System.out.println("Jugador: " + jugador.getNombre());
        System.out.println("Monedas totales: " + jugador.getMonedas());
        System.out.println("Inventario: " + jugador.getInventario());
        System.out.println("====================================");
    }
}
