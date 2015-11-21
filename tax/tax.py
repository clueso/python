FederalTaxRates = [[11138,44701,44700,49185,40000],[0,0.15,0.22,0.26,0.29]];
BCTaxRates = [[9869,37869,37871,11218,18634,45458,151050],[0,0.0506,0.077,0.105,0.1229,0.147,0.168]];

def CalcTaxes(Income, TaxRates):
	TotalTaxes = 0;
	i = 0;
	tmpIncome = Income;
	while (tmpIncome > 0 and i < len(TaxRates[0])):
		if(tmpIncome < TaxRates[0][i]):
			TotalTaxes += tmpIncome * TaxRates[1][i];
			tmpIncome = 0;
		else:
			TotalTaxes += TaxRates[0][i] * TaxRates[1][i];
			tmpIncome -= TaxRates[0][i];
		i += 1; 
	TotalTaxes += tmpIncome * TaxRates[1][len(TaxRates[0])-1];	
	return TotalTaxes;

#print "Income\tWithout split\tWith split\tSaving(%)";
#for Income in range(10000,710000, 10000): 
#	NoSplitTax = CalcTaxes(Income, FederalTaxRates) + CalcTaxes(Income, BCTaxRates);
#	SplitTax = 2 * (CalcTaxes(Income/2, FederalTaxRates) + CalcTaxes(Income/2, BCTaxRates));
#	print Income,"\t",NoSplitTax,"\t",SplitTax,"\t",NoSplitTax-SplitTax;
print CalcTaxes(10000,FederalTaxRates) + CalcTaxes(10000,BCTaxRates);
