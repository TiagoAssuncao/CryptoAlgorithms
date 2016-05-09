import java.util.*;

public class PolynomialCalculator {
	private static Scanner keyboard = new Scanner(System.in);

	private static String firstBinaryPolynomial;
	private static String secondBinaryPolynomial;
	private static String operator;
	private static String result;
	
	private static String xor(String binaryPolynomial1, String binaryPolynomial2) {
		int x, y;
		x = Integer.parseInt(binaryPolynomial1, 2);
		y = Integer.parseInt(binaryPolynomial2, 2);
		int z = x ^ y;
		return intToBinary(z);
	}
	
	private static String division(String obinaryPolynomial1, String binaryPolynomial2) {
		String inverse = inverseMultiplicative(binaryPolynomial2);
		return multiplication(obinaryPolynomial1, inverse);
	}

	private static String inverseMultiplicative(String binary) {
		int inverse = 0;
		int product = 0;

		if(Integer.parseInt(binary)==0)
			return intToBinary(0);

		while(product != 1 && inverse<256) {
			inverse += 1;
			String inv = intToBinary(inverse);
			String prod = multiplication(binary, inv);
			product = Integer.parseInt(prod);
			
		}
		return intToBinary(inverse);
	}

	private static String multiplication(String binaryPolynomial1, String binaryPolynomial2) {
		int firstPolynomial = Integer.parseInt(binaryPolynomial1, 2);
		int secondPolynomial = Integer.parseInt(binaryPolynomial2, 2);
		int product = 0;//product

		for(int i=0; i<8; i++) {
			if(binaryPolynomial2.charAt(7)=='1') {
				product = product ^ firstPolynomial;
			}

			StringBuilder buildSecondPolynomial = new StringBuilder();
			buildSecondPolynomial.append('0');
			
			for(int j=0; j<7; j++) {
				buildSecondPolynomial.append(binaryPolynomial2.charAt(j));
			}
			
			binaryPolynomial2 = buildSecondPolynomial.toString();
			secondPolynomial = Integer.parseInt(binaryPolynomial2, 2);

			StringBuilder buildFirstPolynomial = new StringBuilder();
			for(int j=1; j<8; j++) {
				buildFirstPolynomial.append(binaryPolynomial1.charAt(j));
			}
			
			buildFirstPolynomial.append('0');
			binaryPolynomial1 = buildFirstPolynomial.toString();
			firstPolynomial = Integer.parseInt(binaryPolynomial1, 2);
	
		}
		return intToBinary(product);
	}
	
	private static String intToBinary(int x) {
		String result = Integer.toBinaryString(x);
		if(result.length()<8)
		{
			int pad = 8 - result.length();
			StringBuilder b = new StringBuilder();
			for(int i=0; i<pad; i++)
			{
				b.append('0');
			}
			b.append(result);
			result = b.toString();
		}
		return result;
	}
	
	public static void main(String[] args) {
		
		System.out.println("Enter 8-bits binary polynomials");
		System.out.println("Enter the first binary polynomial: ");
		firstBinaryPolynomial = keyboard.nextLine();
		
		System.out.println("Enter the second binary polynomial: ");
		secondBinaryPolynomial = keyboard.nextLine();

		System.out.println("Enter operator: ");
		operator = keyboard.nextLine();

		if(operator.charAt(0)=='+' || operator.charAt(0)=='-') {
			result = xor(firstBinaryPolynomial, secondBinaryPolynomial); 
		}

		if(operator.charAt(0)=='*') {
			result = multiplication(firstBinaryPolynomial, secondBinaryPolynomial);
		}

		if(operator.charAt(0)=='/') {
			result = division(firstBinaryPolynomial, secondBinaryPolynomial);
		}

		System.out.println("Result:\n" + result);
	}
	
}
