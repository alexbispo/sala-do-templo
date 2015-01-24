import java.util.Scanner;

public class solucao {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int n = scanner.nextInt(); // Recebe valor digitado pelo usuario

		while (n <= 2 && n <= 1000) {
			System.out.println("Digite o numero novamente");
			n = scanner.nextInt();
		}

		System.out.println(new solucao().pecaPerdida(n));

	}

	public int pecaPerdida(int n) {
		Scanner scanner = new Scanner(System.in);

		int pecas[] = new int[n - 1]; 
		int pecaFaltando = 0;
		
		String[] entradaDois = scanner.nextLine().split(" ");

		for (int i = 0; i < pecas.length; i++) { 
			pecas[i] = Integer.parseInt(entradaDois[i]);
		}

		for (int i = 0; i < n; i++) {

			if (getPecaFaltando(pecas, n - i)) {
				pecaFaltando = n - i;
			}
		}

		return pecaFaltando;
	}

	public boolean getPecaFaltando(int pecas[], int n) {
		boolean pecaNaoFoiDigitada = true;

		for (int peca : pecas) {

			if (peca == n) {
				pecaNaoFoiDigitada = false;
			}
		}

		return pecaNaoFoiDigitada;
	}

}