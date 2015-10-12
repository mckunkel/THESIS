{
// define N states
Double_t Nmass4[12] = {938.271998,1008.66491578,1440,1520,1535,1650,1675,1680,1720,2190,2220,2250};
Double_t Nwidth4[12] = {4,4,350,120,150,155,145,130,165,450,400,405};
Double_t Nmass3[3] = {1700,1710,2600}; 
Double_t Nwidth3[3] = {105,95,650};
Double_t Nmass2[6] = {1900,1990,2000,2080,2200,2700};
Double_t Nwidth2[6] = {498,340,200,290,310,390};
Double_t Nmass1[2] = {2090,2100};
Double_t Nwidth1[2] = {335,215};

// define Delta states
Double_t Dmass4[7] = {1232,1620,1700,1905,1910,1950,2420};
Double_t Dwidth4[7] = {125,160,300,355,250,305,395};
Double_t Dmass3[3] = {1600,1920,1930};
Double_t Dwidth3[3] = {345,205,360};
Double_t Dmass2[6] = {1900,2000,2300,2400,2750,2950};
Double_t Dwidth2[6] = {185,210,385,380,415,420};
Double_t Dmass1[6] = {1750,1940,2150,2200,2350,2390};
Double_t Dwidth1[6] = {285,365,130,425,315,280};

// define Lambda states
Double_t Lmass4[9] = {1115.683,1406.5,1519.5,1670,1690,1820,1830,1890,2100};
Double_t Lwidth4[9] = {4,50,15.6,35,60,80,85,100,200};
Double_t Lmass3[5] = {1600,1800,1810,2110,2350};
Double_t Lwidth3[5] = {170,295,175,195,145};
Double_t Lmass2[1] = {2585};
Double_t Lwidth2[1] = {305};
Double_t Lmass1[3] = {2000,2020,2325};
Double_t Lwidth1[3] = {150,155,170};

// define Sigma states
Double_t Smass4[8] = {1189.37,1192.642,1197.449,1385,1670,1775,1915,2030};
Double_t Swidth4[8] = {4,4,4,35.8,55,115,110,180};
Double_t Smass3[4] = {1660,1750,1940,2250};
Double_t Swidth3[4] = {100,90,220,100};
Double_t Smass2[8] = {1560,1580,1620,1690,1880,2080,2455,2620};
Double_t Swidth2[8] = {65,15,70,140,135,190,130,215};
Double_t Smass1[6] = {1480,1770,1840,2000,2070,2100};
Double_t Swidth1[6] = {60,75,110,225,320,120};

// define Cascade states
Double_t Xmass4[3] = {1314.83,1321.31,1530};
Double_t Xwidth4[3] = {4,4,16.1};
Double_t Xmass3[4] = {1690,1820,1950,2030};
Double_t Xwidth3[4] = {10,24,60,20};
Double_t Xmass2[2] = {2250,2370};
Double_t Xwidth2[2] = {50,80};
Double_t Xmass1[3] = {1620,2120,2500};
Double_t Xwidth1[3] = {30,20,100};

// define Omega states
Double_t Omass4[1] = {1672.45};
Double_t Owidth4[1] = {4};
Double_t Omass3[1] = {2250};
Double_t Owidth3[1] = {55};
Double_t Omass2[2] = {2380,2474};
Double_t Owidth2[2] = {26,72};
//Double_t Omass1[0] = {};
//Double_t Owidth1[0] = {};

// use half widths!!!!
for(int i=0;i<12;i++)
	Nwidth4[i] = Nwidth4[i] / 2;
for(int i=0;i<3;i++)
	Nwidth3[i] = Nwidth3[i] / 2;
for(int i=0;i<6;i++)
	Nwidth2[i] = Nwidth2[i] / 2;
for(int i=0;i<2;i++)
	Nwidth1[i] = Nwidth1[i] / 2;
for(int i=0;i<7;i++)
	Dwidth4[i] = Dwidth4[i] / 2;
for(int i=0;i<3;i++)
	Dwidth3[i] = Dwidth3[i] / 2;
for(int i=0;i<6;i++)
	Dwidth2[i] = Dwidth2[i] / 2;
for(int i=0;i<6;i++)
	Dwidth1[i] = Dwidth1[i] / 2;
for(int i=0;i<9;i++)
	Lwidth4[i] = Lwidth4[i] / 2;
for(int i=0;i<5;i++)
	Lwidth3[i] = Lwidth3[i] / 2;
for(int i=0;i<1;i++)
	Lwidth2[i] = Lwidth2[i] / 2;
for(int i=0;i<3;i++)
	Lwidth1[i] = Lwidth1[i] / 2;
for(int i=0;i<8;i++)
	Swidth4[i] = Swidth4[i] / 2;
for(int i=0;i<4;i++)
	Swidth3[i] = Swidth3[i] / 2;
for(int i=0;i<8;i++)
	Swidth2[i] = Swidth2[i] / 2;
for(int i=0;i<6;i++)
	Swidth1[i] = Swidth1[i] / 2;
for(int i=0;i<3;i++)
	Xwidth4[i] = Xwidth4[i] / 2;
for(int i=0;i<4;i++)
	Xwidth3[i] = Xwidth3[i] / 2;
for(int i=0;i<2;i++)
	Xwidth2[i] = Xwidth2[i] / 2;
for(int i=0;i<3;i++)
	Xwidth1[i] = Xwidth1[i] / 2;
for(int i=0;i<1;i++)
	Owidth4[i] = Owidth4[i] / 2;
for(int i=0;i<1;i++)
	Owidth3[i] = Owidth3[i] / 2;
for(int i=0;i<2;i++)
	Owidth2[i] = Owidth2[i] / 2;
//for(int i=0;i<0;i++)
//	Owidth1[i] = Owidth1[i] / 2;

pads("pdgbaryons",1);
pad->SetGrid(0,0);
gN4 = new TGraphErrors(12,Nmass4,Nwidth4,Nwidth4);
gN3 = new TGraphErrors(3,Nmass3,Nwidth3,Nwidth3);
gN2 = new TGraphErrors(6,Nmass2,Nwidth2,Nwidth2);
gN1 = new TGraphErrors(2,Nmass1,Nwidth1,Nwidth1);
//gN4->SetMarkerStyle(21); // box for N states
//gN3->SetMarkerStyle(21);
//gN2->SetMarkerStyle(21);
//gN1->SetMarkerStyle(21);
gN4->SetMarkerColor(kYellow+1);
gN3->SetMarkerColor(kYellow+1);
gN2->SetMarkerColor(kYellow+1);
gN1->SetMarkerColor(kYellow+1);
gN4->SetLineWidth(8); gN4->SetLineColor(kYellow+1);
gN3->SetLineWidth(8); gN3->SetLineColor(kYellow+1);
gN2->SetLineWidth(8); gN2->SetLineColor(kYellow+1);
gN1->SetLineWidth(8); gN1->SetLineColor(kYellow+1);

gD4 = new TGraphErrors(7,Dmass4,Dwidth4,Dwidth4);
gD3 = new TGraphErrors(3,Dmass3,Dwidth3,Dwidth3);
gD2 = new TGraphErrors(6,Dmass2,Dwidth2,Dwidth2);
gD1 = new TGraphErrors(6,Dmass1,Dwidth1,Dwidth1);
//gD4->SetMarkerStyle(22); // triangle for D states
//gD3->SetMarkerStyle(22);
//gD2->SetMarkerStyle(22);
//gD1->SetMarkerStyle(22);
gD4->SetMarkerColor(kOrange);
gD3->SetMarkerColor(kOrange);
gD2->SetMarkerColor(kOrange);
gD1->SetMarkerColor(kOrange);
gD4->SetLineWidth(8); gD4->SetLineColor(kOrange);
gD3->SetLineWidth(8); gD3->SetLineColor(kOrange);
gD2->SetLineWidth(8); gD2->SetLineColor(kOrange);
gD1->SetLineWidth(8); gD1->SetLineColor(kOrange);

gL4 = new TGraphErrors(9,Lmass4,Lwidth4,Lwidth4);
gL3 = new TGraphErrors(5,Lmass3,Lwidth3,Lwidth3);
gL2 = new TGraphErrors(1,Lmass2,Lwidth2,Lwidth2);
gL1 = new TGraphErrors(3,Lmass1,Lwidth1,Lwidth1);
//gL4->SetMarkerStyle(23); // upside-down triangle for L states
//gL3->SetMarkerStyle(23);
//gL2->SetMarkerStyle(23);
//gL1->SetMarkerStyle(23);
gL4->SetMarkerColor(8);
gL3->SetMarkerColor(8);
gL2->SetMarkerColor(8);
gL1->SetMarkerColor(8);
gL4->SetLineWidth(8); gL4->SetLineColor(8);
gL3->SetLineWidth(8); gL3->SetLineColor(8);
gL2->SetLineWidth(8); gL2->SetLineColor(8);
gL1->SetLineWidth(8); gL1->SetLineColor(8);

gS4 = new TGraphErrors(9,Smass4,Swidth4,Swidth4);
gS3 = new TGraphErrors(4,Smass3,Swidth3,Swidth3);
gS2 = new TGraphErrors(8,Smass2,Swidth2,Swidth2);
gS1 = new TGraphErrors(6,Smass1,Swidth1,Swidth1);
//gS4->SetMarkerStyle(20); // disk for S states
//gS3->SetMarkerStyle(20);
//gS2->SetMarkerStyle(20);
//gS1->SetMarkerStyle(20);
gS4->SetMarkerColor(3);
gS3->SetMarkerColor(3);
gS2->SetMarkerColor(3);
gS1->SetMarkerColor(3);
gS4->SetLineWidth(8); gS4->SetLineColor(3);
gS3->SetLineWidth(8); gS3->SetLineColor(3);
gS2->SetLineWidth(8); gS2->SetLineColor(3);
gS1->SetLineWidth(8); gS1->SetLineColor(3);

gX4 = new TGraphErrors(3,Xmass4,Xwidth4,Xwidth4);
gX3 = new TGraphErrors(4,Xmass3,Xwidth3,Xwidth3);
gX2 = new TGraphErrors(2,Xmass2,Xwidth2,Xwidth2);
gX1 = new TGraphErrors(3,Xmass1,Xwidth1,Xwidth1);
//gX4->SetMarkerStyle(29); // star for X states
//gX3->SetMarkerStyle(29);
//gX2->SetMarkerStyle(29);
//gX1->SetMarkerStyle(29);
gX4->SetMarkerColor(kBlue);
gX3->SetMarkerColor(kBlue);
gX2->SetMarkerColor(kBlue);
gX1->SetMarkerColor(kBlue);
gX4->SetLineWidth(8); gX4->SetLineColor(kBlue);
gX3->SetLineWidth(8); gX3->SetLineColor(kBlue);
gX2->SetLineWidth(8); gX2->SetLineColor(kBlue);
gX1->SetLineWidth(8); gX1->SetLineColor(kBlue);

gO4 = new TGraphErrors(1,Omass4,Owidth4,Owidth4);
gO3 = new TGraphErrors(1,Omass3,Owidth3,Owidth3);
gO2 = new TGraphErrors(2,Omass2,Owidth2,Owidth2);
//gO1 = new TGraphErrors(0,Omass1,Owidth1,Owidth1);
//gO4->SetMarkerStyle(24); // circle for O states
//gO3->SetMarkerStyle(24);
//gO2->SetMarkerStyle(24);
//gO1->SetMarkerStyle(24);
gO4->SetMarkerColor(4);
gO3->SetMarkerColor(4);
gO2->SetMarkerColor(4);
//gO1->SetMarkerColor(4);
gO4->SetLineWidth(8); gO4->SetLineColor(4);
gO3->SetLineWidth(8); gO3->SetLineColor(4);
gO2->SetLineWidth(8); gO2->SetLineColor(4);
//gO1->SetLineWidth(8);  gO1->SetLineColor(4);


Double_t xini[2] = {1000,2600};
Double_t yini[2] = {0,230};
gini = new TGraph(2,xini,yini);
//gini->SetTitle("3 and 4-star Baryons: mass vs. width");
gini->SetTitle("");
gini->GetXaxis()->SetTitle("Mass (MeV)");
gini->GetXaxis()->CenterTitle();
gini->GetYaxis()->SetTitle("#Gamma / 2 (MeV)");
gini->GetYaxis()->CenterTitle();
gini->Draw("AP");

//gN1->Draw("PZ");
//gD1->Draw("PZ");
//gS1->Draw("PZ");
//gX1->Draw("PZ");
//gO1->Draw("PZ");

//gN2->Draw("PZ");
//gD2->Draw("PZ");
//gS2->Draw("PZ");
gX2->Draw("PZ");
//gO2->Draw("PZ");


gN3->Draw("PZ");
gD3->Draw("PZ");
gL3->Draw("PZ");
gS3->Draw("PZ");
gX3->Draw("PZ");
//gO3->Draw("PZ");

gN4->Draw("PZ");	// on previous axis, with marker, no ends to error bars
gD4->Draw("PZ");
gL4->Draw("PZ");
gS4->Draw("PZ");
gX4->Draw("PZ");
//gO4->Draw("PZ");

l = new TLegend(0.13,0.55,0.4,0.87);
l.SetBorderSize(0);
l.SetFillStyle(0);
l.SetFillColor(0);
mN = new TMarker(0,0,21);
mD = new TMarker(0,0,21);
mL = new TMarker(0,0,21);
mS = new TMarker(0,0,21);
mX = new TMarker(0,0,21);
//mO = new TMarker(0,0,21);
mN.SetMarkerColor(gN4.GetLineColor());
mD.SetMarkerColor(gD4.GetLineColor());
mL.SetMarkerColor(gL4.GetLineColor());
mS.SetMarkerColor(gS4.GetLineColor());
mX.SetMarkerColor(gX4.GetLineColor());
//mO.SetMarkerColor(gO4.GetLineColor());
mN.SetMarkerSize(2);
mD.SetMarkerSize(2);
mL.SetMarkerSize(2);
mS.SetMarkerSize(2);
mX.SetMarkerSize(2);
//mO.SetMarkerSize(2);

l.AddEntry(mN, "N", "p");
l.AddEntry(mD, "#Delta", "p");
l.AddEntry(mL, "#Lambda", "p");
l.AddEntry(mS, "#Sigma", "p");
l.AddEntry(mX, "#Xi", "p");
//l.AddEntry(mO, "#Omega", "p");
l.Draw();


cout << endl << "Mass        Width" << endl;
cout << "N* states" << endl;
for( Int_t i=0;i<12;i++) {
	cout << Nmass4[i] << "    " << Nwidth4[i] << endl;
}
for( Int_t i=0;i<3;i++) {
	cout << Nmass3[i] << "    " << Nwidth3[i] << endl;
}
cout << "Delta* states" << endl;
for( Int_t i=0;i<7;i++) {
	cout << Dmass4[i] << "    " << Dwidth4[i] << endl;
}
for( Int_t i=0;i<3;i++) {
	cout << Dmass3[i] << "    " << Dwidth3[i] << endl;
}
cout << "Lambda* states" << endl;
for( Int_t i=0;i<9;i++) {
	cout << Lmass4[i] << "    " << Lwidth4[i] << endl;
}
for( Int_t i=0;i<5;i++) {
	cout << Lmass3[i] << "    " << Lwidth3[i] << endl;
}
cout << "Sigma* states" << endl;
for( Int_t i=0;i<8;i++) {
	cout << Smass4[i] << "    " << Swidth4[i] << endl;
}
for( Int_t i=0;i<4;i++) {
	cout << Smass3[i] << "    " << Swidth3[i] << endl;
}
cout << "Cascade* states" << endl;
for( Int_t i=0;i<3;i++) {
	cout << Xmass4[i] << "    " << Xwidth4[i] << endl;
}
for( Int_t i=0;i<4;i++) {
	cout << Xmass3[i] << "    " << Xwidth3[i] << endl;
}
/*
cout << "Omega* states" << endl;
for( Int_t i=0;i<1;i++) {
	cout << Omass4[i] << "    " << Owidth4[i] << endl;
}
for( Int_t i=0;i<1;i++) {
	cout << Omass3[i] << "    " << Owidth3[i] << endl;
}*/


}


