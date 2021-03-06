import java.awt.Color;
import java.awt.Graphics;
import java.awt.Stroke;

public abstract class Lik {
	    protected int x;
	    protected int y;
	    protected Color barvaObrobe;
	    protected Color barvaNotranjosti;
	    protected Stroke tipCrte;
	    
	    public Lik(int x, int y) {
	        super();
	        this.x = x;
	        this.y = y;
	    }
	    
	    public void premakni(int dx, int dy) {
	        this.x += dx;
	        this.y += dy;
	    }
	      
	    public void premakniNa(int x, int y) {
	        this.x = x;
	        this.y = y;
	    }
	    
	    public Color getBarvaObrobe() {
	        return barvaObrobe;
	    }

	    public void setBarvaObrobe(Color barvaObrobe) {
	        this.barvaObrobe = barvaObrobe;
	    }

	    public Color getBarvaNotranjosti() {
	        return barvaNotranjosti;
	    }

	    public void setBarvaNotranjosti(Color barvaNotranjosti) {
	        this.barvaNotranjosti = barvaNotranjosti;
	    }
	    
	    public abstract void narisiSe(Graphics g);
}
