fontmake -o ttf-interpolatable -m RobotoFlex.designspace --no-production-names --subset
fonttools varLib RobotoFlex.designspace
mv RobotoFlex-VF.ttf ../fonts/RobotoFlex-VF.ttf
