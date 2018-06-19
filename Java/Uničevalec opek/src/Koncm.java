import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Koncm extends JPanel implements ActionListener {
	protected JButton gumb1;
	private Okno okno;
	public JLabel info;
	
	public Koncm(Okno okno) {
		super();
		this.okno = okno;
		this.setBackground(Color.white);
		info = new JLabel();
		info.setText("");
		add(info);
		gumb1 = new JButton("Ponovno igraj");
		add(gumb1);
		gumb1.addActionListener(this);
		 
	}
	
	@Override
    public Dimension getPreferredSize() {
        return new Dimension(700, 900);
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		if (event.getSource() == gumb1) {
			okno.pokaziPlatno(this);
		}
		
	}
	

}
