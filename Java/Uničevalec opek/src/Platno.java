import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.geom.Area;
import java.awt.geom.Ellipse2D;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JPanel;
import javax.swing.Timer;

public class Platno extends JPanel implements MouseMotionListener, MouseListener, ActionListener {
	 private List<Lik> liki;
	 private Opeka opeka;
	 private Odbijac odbijac;
	 private Unicevalka unicevalka;
	 private Boolean zacetek = true;
	 private Timer animacijskiTimer;
	 private List<Opeka> opeke;
	 private Okno okno;
	
	 
	public Platno(Okno okno) {
		super();
		this.okno = okno;
		this.setBackground(Color.white);
	    addMouseMotionListener(this);
	    addMouseListener(this);
	    liki = new ArrayList<Lik>();
	    
	    //dodamo odbijac
        odbijac = new Odbijac(300, 820, 50, 20);
        liki.add(odbijac);
        
        //dodamo zogico
        unicevalka = new Unicevalka(350, 813,7, this);
        liki.add(unicevalka);
        
        // dodamo opeko
        int xo = 90;
        int yo = 40;
        opeke = new ArrayList<Opeka>();
        for (int i = 1; i < 4; i++){
        	for (int j = 1; j < 6; j++){
        		System.out.println(i + " " + j);
        		Opeka opek = new Opeka(xo, yo, this);
        		opeke.add(opek);
        		xo = xo + 105;
        	}
        	xo = 90;
        	yo = yo + 45;
        }
        animacijskiTimer = new Timer(5, this);
        animacijskiTimer.start();
	}

    public void dodajLik(Lik lik) {
        liki.add(lik);
    }
    
    public void brisi() {
        liki.clear();
        repaint();
    }
	
	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		for(Lik lik: this.liki) {
            lik.narisiSe(g);
        }
		for(Opeka opeka: this.opeke) {
            opeka.narisiSe(g);
        }
	}
	
	@Override
    public Dimension getPreferredSize() {
        return new Dimension(700, 900);
	}

	@Override
	public void mouseMoved(MouseEvent e) {
		odbijac.x = e.getX() - 50;
		if (zacetek) {
			unicevalka.x = e.getX();
		}
		repaint();
	}
	
	
	@Override	
	public void mouseClicked(MouseEvent e){
		if (zacetek == true){
			zacetek = false;
			unicevalka.izstrel(e.getX());
		}
	}
	
	@Override
	public void mouseDragged(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		if (zacetek == true){
			zacetek = false;
			unicevalka.izstrel(e.getX());
		}
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	public void actionPerformed(ActionEvent e) {
        if(e.getSource() == this.animacijskiTimer) {
        	Area kroglica = new Area(new Ellipse2D.Double(unicevalka.x - unicevalka.r, unicevalka.y - unicevalka.r, 2 * unicevalka.r, 2 * unicevalka.r));
        	// odboj od odbijaca
        	if (kroglica.intersects(odbijac.x, odbijac.y, 100, 20)){
        		unicevalka.premik_y *= -1;
        	}
        	// odboj od opek
        	for (Opeka opeka: this.opeke) {
            	if (kroglica.intersects(opeka.x, opeka.y, 100, 40)){
            		if ((opeka.x <= unicevalka.x) && (unicevalka.x <= opeka.x + 100)){
            			unicevalka.premik_y *= -1;
            		}
            		else if ((opeka.y  <= unicevalka.y) && (unicevalka.y <= opeka.y + 40)){
            			unicevalka.premik_x *= -1;
            		}
            		opeke.remove(opeka); // brisanje opek
            		break;
            	}
        	}
        	
        	
        	// odboj od sten
            if (((unicevalka.x - unicevalka.r + unicevalka.dx*unicevalka.premik_x) < 0) || 
            		((unicevalka.x + unicevalka.r + unicevalka.dx*unicevalka.premik_x) > 700)) {
            	unicevalka.premik_x *= -1;
            	
            }
            if ((unicevalka.y - unicevalka.r + unicevalka.dy*unicevalka.premik_y) < 0) {
            	//System.out.println("Y meja " + unicevalka.y + "  //  " + (unicevalka.y - unicevalka.r - unicevalka.dy*unicevalka.premik_y));
            	unicevalka.premik_y *= -1;
            	//premikY = -(unicevalka.y - unicevalka.r);
            }
            if  ((unicevalka.y + unicevalka.r - unicevalka.dy*unicevalka.premik_y) > 900){
            	//System.out.println("KONEC");
            }
            if (unicevalka.y > 920) {
            	animacijskiTimer.stop();
            	okno.pokazikonMeni();
            	okno.koncm.info.setText("Bravo, zelo si slab!");
            }
            int premikX = unicevalka.dx*unicevalka.premik_x;
        	int premikY = unicevalka.dy*unicevalka.premik_y;
            unicevalka.premakni(premikX, premikY);
            //System.out.println("to je X  " + unicevalka.dx*unicevalka.premik_x + " in y " + unicevalka.dy*unicevalka.premik_y);
            if (opeke.size() != 0){
            	repaint();
            }
            else{
            	animacijskiTimer.stop();
            	okno.pokazikonMeni();
            	okno.koncm.info.setText("Bravo, zelo si dober!");
            }
            return;
        }
	}
}
