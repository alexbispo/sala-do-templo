import java.util.Scanner;

public class solucao {
	
	public static void main ( String[] args) {
		Scanner reader = new Scanner(System.in);
		
		int[][] ret_um = new int[2][2];
		int[][] ret_dois = new int[2][2];
		
		String[] entradas_um = reader.nextLine().split(" ");
		
		ret_um[0][0] = Integer.parseInt(entradas_um[0]);
		ret_um[0][1] = Integer.parseInt(entradas_um[1]);
		ret_um[1][0] = Integer.parseInt(entradas_um[2]);
		ret_um[1][1] = Integer.parseInt(entradas_um[3]);
		
		String[] entradas_dois = reader.nextLine().split(" ");
		
		ret_dois[0][0] = Integer.parseInt(entradas_dois[0]);
		ret_dois[0][1] = Integer.parseInt(entradas_dois[1]);
		ret_dois[1][0] = Integer.parseInt(entradas_dois[2]);
		ret_dois[1][1] = Integer.parseInt(entradas_dois[3]);		
		
		System.out.println(new solucao().verificarColisoes(ret_um, ret_dois));
			
		
	} // fecha main
	
	public int verificarColisoes(int[][] ret1, int[][] ret2) {
		int f = 0;
		
		if ((ret1[0][1] >= ret2[0][1] && ret1[0][1] <= ret2[1][1]) || (ret2[0][1] >= ret1[0][1] && ret2 [0][1] <= ret1[1][1]) ||
		(ret1[0][1] >= ret2[0][1] && ret1[1][1] <= ret2[1][1]) || (ret2[0][1] >= ret1[0][1] && ret2[1][1] <= ret1[1][1])) {
			if ((ret1[0][0] >= ret2[0][0] && ret1[0][0] <= ret2[1][0]) || (ret2[0][0] >= ret1[0][0] && ret2[0][0] <= ret1[1][0]) ||
			(ret1[0][0] >= ret2[0][0] && ret1[1][0] <= ret2[1][0]) || (ret2[0][0] >= ret1[0][0] && ret2[1][0] <= ret1[1][0])) {
				f = 1;
			}
		} 
		
		return f;
	} // fecha verificarColisoes
	
} // fecha Solucao
