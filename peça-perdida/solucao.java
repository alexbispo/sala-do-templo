import java.util.Scanner;


public class solucao {
	
	static Scanner scanner = new Scanner(System.in); 
	int pecaFaltando = 0; 
	
	public static void main(String[] args) {
		System.out.println("Digite um numero entre 2 e 1000");
		int n = scanner.nextInt();
		
		if (n <= 1 || n > 1000) {
			System.out.println("Digite um numero entre 2 e 1000");
			n = scanner.nextInt();
		}
		
		int pecaFaltando = new solucao().setPecasDoQuebraCabeca(n);
		
		System.out.println(pecaFaltando);
	}
	
	
	public int setPecasDoQuebraCabeca(int n){
		
		int arrayPecas [] = new int [n]; 
		int pecasDoQueBraCabeça = 0; 
		
		for (int i = 1; i < n; i++) {
			System.out.println("Digite as pecas");
			pecasDoQueBraCabeça = scanner.nextInt();
			
			if (pecasDoQueBraCabeça > n ) {
				System.out.println("Digite as peças menores que: " +  n);
				pecasDoQueBraCabeça = scanner.nextInt();
			}
			
			arrayPecas [i] = pecasDoQueBraCabeça;
		}
		
		return getPecaFaltando(arrayPecas, n);
	}
	
	public int getPecaFaltando(int[]arrayPecas, int n){
		
		int indiceArray = n - 1; 
		
		for (int i = 0; i < arrayPecas.length; i++) {
			
			if (arrayPecas[indiceArray - i] !=  n - i) {
				pecaFaltando = n - i; 
				break;
			} 
		}
		
		return pecaFaltando; 
	}

}
