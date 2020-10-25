import java.io.IOException;

public class ReadInput {
    public static void main(String[] args) throws IOException {
        System.out.println("Enter your first byte");
        int inByte = System.in.read();
        System.out.println("The first byte that you typed: " + (char)inByte);
        System.out.printf("%s: %c.%n", "The first byte that you typed", inByte);
    }
}