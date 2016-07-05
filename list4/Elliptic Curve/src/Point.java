
public class Point {
	
	public int x,y;
	
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj == this) {
			return true;
		}
		if(!(obj instanceof Point)) {
			return false;
		}
		Point p = (Point) obj;
		return p.x == this.x && p.y == this.y; 
	}
	

}