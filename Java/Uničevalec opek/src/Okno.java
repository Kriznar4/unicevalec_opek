import java.awt.BorderLayout;
import java.awt.Container;
import java.util.ArrayList;
import java.util.List;

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
	
    public static void main(String[] args) {
        //mojiLiki.add(new Krog(150, 150, 20));
        JFrame okno = new Okno();
        okno.pack();
        okno.setVisible(true);
    }
}
