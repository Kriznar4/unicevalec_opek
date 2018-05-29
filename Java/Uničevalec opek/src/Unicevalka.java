import java.awt.Color;
import java.awt.Graphics;

public class Unicevalka extends Lik{
	private int r; 
	private Platno platno;
	int hitrost = 7;
	int premik_x = 1;
	int premik_y = 1;
	double alfa;
	int dx;
	int dy;
    
    public Unicevalka(int x, int y, int r, Platno platno) {
    	super(x,y);
    	this.platno = platno;
        this.r = r; 
    }

    @Override
    public void narisiSe(Graphics g) {
        g.setColor(Color.BLACK);
        g.drawOval(x - r, y - r, 2*r, 2*r); 
    }

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }
    
	public void izstrel(int x) {
		if (x < 350) {
			premik_x *= -1;
		}
		alfa = Math.atan(Math.abs(262)/Math.abs(350 - x));
		dx = (int) (Math.cos(alfa)*hitrost);
		dy = (int) (Math.sin(alfa)*hitrost);
	}

}
