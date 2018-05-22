import java.awt.*;

import javax.swing.JPanel;

public class Platno extends JPanel  {
	
	public Platno() {
		super();
	}
	
	@Override
    public Dimension getPreferredSize() {
        return new Dimension(1000, 1000);
	}
	
	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		setBackground(Color.WHITE);
	}
}
