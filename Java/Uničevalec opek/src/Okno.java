import java.awt.BorderLayout;
import java.awt.Container;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Okno extends JFrame {
	private Platno platno;
	private Zacm zacm;
	
	public Okno() {
		super();
		setLayout(new BorderLayout());
		Zacm zacm = new Zacm(this);
		add(zacm, BorderLayout.NORTH);
		//zacm.setVisible(false);
		platno = new Platno();
		add(platno, BorderLayout.SOUTH);
		platno.setVisible(false);
		//zacm.setVisible(true);

	}
	
	public void pokaziPlatno(JPanel kateri){
		kateri.setVisible(false);
		platno.setVisible(true);
		
		
	}
}
