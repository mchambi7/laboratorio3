import java.util.Scanner;

public class Prog1018 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        if (sc.hasNextInt()) {
            int t = sc.nextInt();

            for (int i = 0; i < t; i++) {
                long a = sc.nextLong();
                long b = sc.nextLong();

                if (a > b) {
                    System.out.println(">");
                } else if (a < b) {
                    System.out.println("<");
                } else {
                    System.out.println("=");
                }
            }
        }
        sc.close();
    }
}