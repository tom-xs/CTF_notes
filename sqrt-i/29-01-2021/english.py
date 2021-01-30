flag=("REDACTED")
x=0
for char in flag:
	x = x + int(ord(char))	

print(str(2**x)) #266764024533620246048487657206788853953854304413951065278542892989315210011739621162804595721735095941943617236993261550230730140922038450941823819782415079187396498423963087058253937044194492876153670651104294571459417724261698913254252972257288089272187773996988908537071765695567285922175569842556316025764603292918233436243662170766137356297554266414441651962986107906284435113575338522084869006241092254861344490704853717260971927689670251330862582003371781698568686425005489363468214217267312793634323923220077915348177066903474029761667234974020307013991040541809588242953756521232131415480548844689140012202669850605076561152971854496521235595769271430802572146320905139558123885814768665865777754437659333036445817158731744615751881201148288283798750712102329205990348443052857392445961200373353498907226001312082434234842689980076529479796736994145605584268282821773250002944

'''
the rsa below is meant to be used for verification purposes only. To verify, please substitute your `flag`, and make sure it is equal to c.
'''
n = 695688466590534955454148421165861757178336233175751119839564112892231817219672087510890290800675284025626309281541930296119606088753094906888977520346624586374670053961583114371912956507715741067608642447785172442890230796247988671281863914327023177156464447431496902175223451768017646255774099255149382472428016351873178887050893191085781331845758408212790695492371239387643715821949926240530229039834605096026289782268367011343518368092142114308780684823189333504260333522503439103459552505850188092399929917841344292921317305445490798344022547299584623805514199029985545518703241808996873418107929260006967876821896270587071094709592557702996998849160989160935084914818697747466991606604735363872679034488892307939043187479603261769047999258617242241976052552702974823962358268563033626119612910120843848552720432709850145330463910257149741377378812552206239656266841827060144409621440392478253026894175358187391438570625948622052990782929377059691211552789058071992155816776561407054355031770583599471277112502462875075225369957496235791978767160953345882581169576883785417622074571915960345493553851332664016229992155937382592528963013921055071132436500350154159557217329202335774428374701686355745029550963482291114898537283429621645037853162689348822555595954662258845906917214718662763088134417021155489164753110814235065256182233811689079095473042154087052001526439286525385659350778907468177788728702614996054014207821774051861705581134782467221903509804000556110606410176115094481215019692519218015559846108243547968152064470810582514184099812285014197280810843698976366980192844452535130356537583109788396717585872785524914311623270975629781502016235975703908669321600528385306571944826817099443439794060041901867832353035619814818761753561221238496806158578984963396965361396293124022337253491
e = 65537
ct = int.from_bytes(flag.encode('utf-8'), byteorder='big')
ct_enc = pow(ct, e, n)

c = 14463833055831170178367007689057406072095555444338339847433702766181378071542657176346784205887401098025736990433125351531647865808524641974418933500970975168329409842608303177254770904633818246473739463309178987070398198917171066757408151888573532301502723663435702527428133431495592568957357940431349414886151167625440271371787521281327009269211878170075246427297733578930967304409241733885890170814187663059205974272535078431096906876217898326858203582387475898304527529816994816208791822192318778756252805344794540562248650016486620045526363157081412993169901201731927817694718945772187611449248643283088570094403847323059875298557036883504155847724196233549853324979689383092726785290572894815054978977803451754920691015616639708827560078015156669968326699863142344158481219106352156514882179479272838719551092153693998214673035008100284725193464803102139979445443100985457408804103136580393967542832246223143730178319405774378125440458305745619596215697188738151376118764373763054818357751596140742270329594379244015210953100307304761130160554709012132199006827086803309468903639774513676385827735241762287294603129409763539850801661552010878773612132860049280210004148676375030798880278318039383299579396299366992816821615449041703642922776602477714492731528258353361149192537166774780383066303838780091520811255862217822747655424123163643043673108605945745405907700365777530519311277081249913184695341905302998637967373999766919886239326990078687298806959645146018822327520647937193606845543391376028849789833407253546889363632449545716887542624930905586584269117496463507832674289186200354453609497195832121205806358723023213847798550833131714588357464718018367554052556832926528305765037055992169489388818439734318200992021098734144202150180423182935698870910985608442419813971492782099471314902

print(ct_enc)

'''
meu codigo
'''
#filtrar palavras grandes
with open("sqrt-i\\29-01-2021\wordList.txt",'r') as arquivoRead:
	with open("sqrt-i\\29-01-2021\wordListFiltered.txt",'w') as arquivoWrite:
		for linha in arquivoRead:
			if len(linha) > 4 :
				arquivoWrite.write(str(linha))
