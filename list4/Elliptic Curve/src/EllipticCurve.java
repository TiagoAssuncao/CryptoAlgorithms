import java.util.ArrayList;

public class EllipticCurve {

	public static void main(String[] args) {

		Curve curve = new Curve(2433, 24527, 132529);

		ArrayList<Point> all = curve.findAllPoints();

		System.out.println("\n\nNúmero total de pontos: " + all.size());

		ArrayList<Integer> orders = new ArrayList<Integer>();
		System.out.println("Pontos de maior e menor ordem:");
		
		for (Point p : all) {
			
			int order = curve.findOrder(p);

			if (!orders.contains(order)) {
				orders.add(order);
				System.out.println("(" + p.x + ", " + p.y + ")" + "\tOrdem: " + order);
			}
		}
	}

}