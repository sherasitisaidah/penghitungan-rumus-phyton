import java.util.Scanner;

public class PenghitungRumus {
    public static void hitungLuasSegitiga() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan panjang alas segitiga: ");
        double alas = scanner.nextDouble();
        System.out.print("Masukkan tinggi segitiga: ");
        double tinggi = scanner.nextDouble();
        double luas = 0.5 * alas * tinggi;
        System.out.println("Luas segitiga adalah: " + luas);
    }

    public static void hitungLuasPersegiPanjang() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan panjang persegi panjang: ");
        double panjang = scanner.nextDouble();
        System.out.print("Masukkan lebar persegi panjang: ");
        double lebar = scanner.nextDouble();
        double luas = panjang * lebar;
        System.out.println("Luas persegi panjang adalah: " + luas);
    }

    public static void cekGanjilGenap() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan angka: ");
        int angka = scanner.nextInt();
        if (angka % 2 == 0) {
            System.out.println(angka + " adalah angka genap");
        } else {
            System.out.println(angka + " adalah angka ganjil");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Hitung luas segitiga");
            System.out.println("2. Hitung luas persegi panjang");
            System.out.println("3. Menentukan angka ganjil dan genap");
            System.out.println("4. Quit");

            System.out.print("Masukkan pilihan menu: ");
            int pilihan = scanner.nextInt();

            switch (pilihan) {
                case 1:
                    hitungLuasSegitiga();
                    break;
                case 2:
                    hitungLuasPersegiPanjang();
                    break;
                case 3:
                    cekGanjilGenap();
                    break;
                case 4:
                    System.out.println("Terima kasih telah menggunakan program ini.");
                    System.exit(0);
                default:
                    System.out.println("Pilihan tidak valid. Silakan pilih menu yang benar.");
            }
        }
    }
}