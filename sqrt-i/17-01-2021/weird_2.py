from decimal import *
from sympy import mod_inverse, crypto
from sympy.ntheory import reduced_totient
import binascii


getcontext().prec = 999
n = 1227173678549949481481779866763773386187676840178483511553906049903330196981504886366294050093311011086664701234281866417764837848162645000249537380395979992437992259294790825818148318151924517511659338434866935790375158108998482756277690583781840889677345463523584003134410504180030356076085421418063496016608562482653076102159866832051187558432563622650124735137698397654121502954359877239374327846807555131779396503508683063781694094360624781072150085466080816172259064267050716628664621838769974685957341228098571770893475329733419863097013686853960591990460762389595000741855739472070530091965323319645724187857
e = 65537
ciphertext = 886307356132225534225669501252669518370960197125891229224634935752449645036920189818280636888373386077722802602631663071287677160036776078863484485914584512245207252833007857895496631042763290138216136079591476092522643285304625895296001899814094788365968999078205199260380689855550410895776216936564460518519299807379454864353651309372733769298403852305845270673020228793187811960794686768143622667100319594413956357768725600551533146328072825408309274197145267207935182221305586153488038911345857243817618302352468584989054675719602300483904895599192811625022064548570758651279897286697655334546845910931035950788

x = Decimal(2267901176829050997429527376207596570482304361304439696030245886507034572470411385071427874779635586054001458549876019754020879201764536580169968998939724117286359380163800233991495863413529575722262456772880142150111735415182931401421708780530866047388580348120906412809280308073259759076080922922213287407957121014364591542164644116254749459899139411079712681856164107867467514566287926787426904741372401675142015650690280642136112126217528730588114420023319366486467796503794850264015415039370114753098499977654251174371500102934858665665014862453008297939299508166630358964901597527659195164800650828224457848907768983512486607728444944019017962620290064164752690745815483988378419887390312051265456320609411767027205107077124226829093581097885782123983496935579299947397134743086000725497455788880038653423812960997656067127864375027902595063845926183589747528022126214627404381470411235454056835016005729082670158425280186501341799610019525890309639860154946159830401724970062000372374340308565141477471049874049679696806395568208897507861311259225085968738980719732916678926922837788014096626745574271176974487139136115371329319178523209389422750235958237186849433075836893722215861142644336580814862075339120839770335496715627918769523833470061580263029729627811125707025192024984654641339213270180505874637903263918673488914865186940960500601784777817904607606918458412629266859447902838104205029651590539522272208302021184878689735986889851546956706787348506729016572795047120364884713135946065378105229304919892602526415205275156247921005012699740310842846589489391018664738826742715473597353190365734308014705164752095328888411263820218666235297865999625109957313384939794903039882977057414692006228460273303450833871299223979815176725443060109341622942261007474139592582430728701381343616235046790929916020042946148306990593297140807353808396435197201184320424540540876169065689605122585453741765346558519419526746267613802364500530610748989401781136966893400718729173335386976459711768469235503870502133140455524729951135712915951310919680072348020093209937840735157875691411721524216435531790476791210177170979624830675549452540319365387278515224344520535074658761176477148227673499164113375997896907923591223935804857551312382209483695659432651840831296906854188213415492956880420584026144154889514920505188953582140643715746425110580231448730877967855569559101023626963719605153773878208072912967343034569259383590717759431411892666913771624649)

phi = int((x.sqrt()/n)+1)

d = mod_inverse(e,phi)

private_key = (n,d)

msg = crypto.decipher_rsa(i = ciphertext,key = private_key)

print("cipher Decrypted = "+ str(msg))

k = binascii.unhexlify(format(msg, 'x')).decode()
print(".flag "+k)