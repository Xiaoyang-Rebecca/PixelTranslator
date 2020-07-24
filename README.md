# PixelTranslator
 We use cGAN to fillin the synthetic colors on gray images of border/vein. And evaluated the reconstruction accuracy by leaf types classification using Alexnet CNN Protopytpe of generate fake image from hand-drawn vein has also been proposed.



－ Step 1. Vein detection (Pre-processing)

－ Step 2. GAN            (GAN reconstruction using pre-processed image)

－ Step 3. CNN            (Classification using Alexnet)


Addition: Interactive Interface, allows to draw images in real time, and get GAN reconstruction, and classification using CNN. 

Code adapted from cycleGAN https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix


Task Distribution

Group Member |	Contributions
------| -----
Rachel Mills |	Literature review, dataset assembly | report compilation
Raj Shah |	GAN model study, GAN result analysis, report compilation
Xiaoyang Li |	Image preprocessing, GAN code review, GAN implementation
Gaurav Roy |	CNN model study, CNN result analysis, report compilation
Aditi Singh	| GAN code review, CNN implementation, Interactive Interface building
