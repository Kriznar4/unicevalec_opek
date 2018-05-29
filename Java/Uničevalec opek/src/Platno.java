import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JPanel;
import javax.swing.Timer;

public class Platno extends JPanel implements MouseMotionListener, MouseListener, ActionListener {
	 private List<Lik> liki;
	 private Odbijac odbijac;
	 private Unicevalka unicevalka;
	 private Boolean zacetek = true;
	 private Timer animacijskiTimer;
	
	 
	public Platno() {
		super();
		this.setBackground(Color.white);
	    addMouseMotionListener(this);
	    addMouseListener(this);
	    liki = new ArrayList<Lik>();
        odbijac = new Odbijac(300, 820, 50, 20);
        liki.add(odbijac);
        unicevalka = new Unicevalka(350, 813,7, this);
        liki.add(unicevalka);
        animacijskiTimer = new Timer(20, this);
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
		zacetek = false;
	}
	
	@Override
	public void mouseDragged(MouseEvent e) {
		// TODO Auto-generated method stub
		zacetek = false;
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
		zacetek = false;
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		zacetek = false;
	}
	
	public void actionPerformed(ActionEvent e) {
        if(e.getSource() == this.animacijskiTimer) {
            unicevalka.premakni(unicevalka.dx*unicevalka.premik_x, unicevalka.dy*unicevalka.premik_y);
            repaint();
            return;
        }
	}
}
