
import java.awt.Color;
import java.awt.Graphics;


public class Odbijac extends Lik {
	int sredina = 350;
	//int odmik = 50;
	//int visina = 20;
	int odmik;
	int visina;

	public Odbijac(int x, int y, int odmik, int visina) {
	    super(x, y);
	    this.odmik = odmik;
	    this.visina = visina;
	}
	
	@Override
	public void narisiSe(Graphics g) {
		g.setColor(Color.BLUE);
	    g.fillRect(x, y, 2*odmik, visina);
	}
}
