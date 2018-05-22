import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;

public class Koncm extends JPanel implements ActionListener {
	protected JButton gumb1;
	private Okno okno;
	
	public Koncm(Okno okno) {
		super();
		this.okno = okno;
		gumb1 = new JButton("Ponovno igraj");
		add(gumb1);
		gumb1.addActionListener(this);
		 
	}
	
	@Override
    public Dimension getPreferredSize() {
        return new Dimension(1000, 1000);
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		if (event.getSource() == gumb1) {
			okno.pokaziPlatno(this);
		}
		
	}
	

}
