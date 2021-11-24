import numpy as np

ALL=[3979839.0,
3993789.0,
3996688.0,
4005632.0,
4013808.0,
4020587.0,
4039667.0,
4044777.0,
4068495.0,
4071643.0,
4080180.0,
4087125.0,
4093412.0,
4102252.0,
4115342.0,
4127158.0,
4137062.0,
4144165.0,
4149832.0,
4155160.0,
4162437.0,
4173357.0,
4183672.0,
4192606.0,
4199029.0,
4204300.0,
4209098.0,
4216507.0,
4228774.0,
4239773.0,
4249061.0,
4255543.0,
4260494.0,
4265001.0,
4272764.0,
4284400.0,
4295876.0,
4305634.0,
4312528.0,
4318437.0,
4323346.0,
4331274.0,
4343591.0,
4355169.0,
4366833.0,
4375253.0,
4382019.0,
4388581.0,
4410921.0,
4429723.0,
4447231.0,
4462324.0,
4466173.0,
4476078.0,
4485437.0,
4516839.0,
4545665.0,
4553744.0,
4591264.0,
4608512.0,
4607958.0,
4619273.0,
4649964.0,
4684462.0,
4722102.0,
4755887.0,
4779675.0,
4792463.0,
4816177.0,
4857463.0,
4908540.0,
4957374.0]

ISR=[1082981.0,
1096881.0,
1104971.0,
1112964.0,
1117596.0,
1117596.0,
1117596.0,
1139887.0,
1145932.0,
1154286.0,
1165682.0,
1172253.0,
1184053.0,
1194783.0,
1202212.0,
1208403.0,
1211443.0,
1220397.0,
1228129.0,
1235064.0,
1242262.0,
1247633.0,
1254351.0,
1256600.0,
1262945.0,
1266206.0,
1270230.0,
1274395.0,
1277270.0,
1282218.0,
1285570.0,
1287977.0,
1290129.0,
1293498.0,
1296343.0,
1298589.0,
1300968.0,
1302777.0,
1304356.0,
1305711.0,
1307870.0,
1309738.0,
1311295.0,
1312908.0,
1314213.0,
1315317.0,
1316317.0,
1317758.0,
1319001.0,
1319902.0,
1320962.0,
1321894.0,
1322395.0,
1323079.0,
1324040.0,
1324897.0,
1325496.0,
1326171.0,
1326742.0,
1327126.0,
1327458.0,
1328218.0,
1331597.0,
1332247.0,
1332801.0,
1333263.0,
1333605.0,
1333989.0,
1334766.0,
1335184.0,
1335654.0,
1336174.0]

ITA=[4546487.0,
4553241.0,
4559970.0,
4566126.0,
4571440.0,
4574787.0,
4579502.0,
4585423.0,
4590941.0,
4596558.0,
4601749.0,
4606413.0,
4609205.0,
4613214.0,
4618040.0,
4623155.0,
4627699.0,
4632275.0,
4636111.0,
4638516.0,
4641890.0,
4645853.0,
4649906.0,
4653696.0,
4657215.0,
4660314.0,
4662087.0,
4665049.0,
4668261.0,
4672355.0,
4675758.0,
4679067.0,
4682034.0,
4683646.0,
4686109.0,
4689341.0,
4692274.0,
4695291.0,
4698038.0,
4700316.0,
4701832.0,
4704318.0,
4707087.0,
4709753.0,
4712482.0,
4715464.0,
4717899.0,
4719493.0,
4722188.0,
4725887.0,
4729678.0,
4733557.0,
4737462.0,
4741185.0,
4743720.0,
4747773.0,
4752368.0,
4757231.0,
4762563.0,
4767440.0,
4771965.0,
4774783.0,
4777614.0,
4782802.0,
4788704.0,
4795465.0,
4802225.0,
4808047.0,
4812594.0,
4818705.0,
4826738.0,
4835435.0]

NOR=[161814.0,
163364.0,
165051.0,
166200.0,
167265.0,
168469.0,
170173.0,
171719.0,
173348.0,
174649.0,
175489.0,
176142.0,
177262.0,
178481.0,
179450.0,
180432.0,
181195.0,
181765.0,
182239.0,
182918.0,
183402.0,
184609.0,
185330.0,
186035.0,
186554.0,
186935.0,
187593.0,
188295.0,
188850.0,
189431.0,
189915.0,
190224.0,
190533.0,
191017.0,
191599.0,
192079.0,
192587.0,
193054.0,
193275.0,
193562.0,
193734.0,
194630.0,
195029.0,
195385.0,
195808.0,
196142.0,
196351.0,
196896.0,
197504.0,
198161.0,
198909.0,
199550.0,
200093.0,
200517.0,
201410.0,
202554.0,
203734.0,
204730.0,
205855.0,
206653.0,
207280.0,
208615.0,
210241.0,
211755.0,
213289.0,
214795.0,
215857.0,
216855.0,
218387.0,
220513.0,
222296.0,
224302.0]

RUS=[6838652.0,
6857243.0,
6875713.0,
6894113.0,
6912375.0,
6929862.0,
6946922.0,
6964595.0,
6982628.0,
7000636.0,
7019200.0,
7037435.0,
7055296.0,
7072825.0,
7091368.0,
7110656.0,
7130245.0,
7150244.0,
7170069.0,
7189445.0,
7208241.0,
7227549.0,
7248572.0,
7269514.0,
7291097.0,
7313112.0,
7334843.0,
7355883.0,
7377774.0,
7401104.0,
7425057.0,
7449689.0,
7474850.0,
7500000.0,
7524465.0,
7548944.0,
7575825.0,
7602386.0,
7631034.0,
7658923.0,
7687559.0,
7714973.0,
7742899.0,
7773388.0,
7804750.0,
7837101.0,
7870529.0,
7903963.0,
7936798.0,
7969960.0,
8005376.0,
8041581.0,
8078309.0,
8112999.0,
8149946.0,
8185400.0,
8220975.0,
8260045.0,
8298850.0,
8338053.0,
8377984.0,
8417305.0,
8455232.0,
8494589.0,
8533706.0,
8573323.0,
8613533.0,
8651561.0,
8689818.0,
8727817.0,
8764713.0,
8804297.0]

FRA=[6868151.0,
6882305.0,
6897529.0,
6910865.0,
6921275.0,
6924325.0,
6938866.0,
6944797.0,
6962917.0,
6972934.0,
6982683.0,
6990662.0,
6992980.0,
7007436.0,
7007819.0,
7022203.0,
7029959.0,
7037931.0,
7043875.0,
7045422.0,
7054198.0,
7061323.0,
7068630.0,
7075305.0,
7080675.0,
7085607.0,
7087110.0,
7094334.0,
7100572.0,
7106028.0,
7111154.0,
7116415.0,
7120214.0,
7121507.0,
7127454.0,
7137177.0,
7142387.0,
7147186.0,
7152009.0,
7156066.0,
7157206.0,
7163317.0,
7164924.0,
7174580.0,
7180773.0,
7185744.0,
7189566.0,
7190716.0,
7196754.0,
7202840.0,
7209126.0,
7215584.0,
7221941.0,
7226974.0,
7228331.0,
7235100.0,
7242180.0,
7248285.0,
7254779.0,
7262178.0,
7268527.0,
7270410.0,
7272516.0,
7282823.0,
7292220.0,
7301303.0,
7310967.0,
7319526.0,
7321767.0,
7334332.0,
7346277.0,
7358920.0]

CHI=[94989.0,
95017.0,
95045.0,
95073.0,
95091.0,
95127.0,
95146.0,
95174.0,
95191.0,
95216.0,
95262.0,
95311.0,
95403.0,
95476.0,
95556.0,
95640.0,
95686.0,
95752.0,
95801.0,
95873.0,
95914.0,
95957.0,
96011.0,
96051.0,
96081.0,
96116.0,
96148.0,
96177.0,
96199.0,
96233.0,
96274.0,
96302.0,
96329.0,
96358.0,
96385.0,
96410.0,
96432.0,
96451.0,
96475.0,
96500.0,
96512.0,
96534.0,
96560.0,
96565.0,
96579.0,
96600.0,
96627.0,
96648.0,
96678.0,
96699.0,
96747.0,
96792.0,
96836.0,
96874.0,
96937.0,
96976.0,
97015.0,
97079.0,
97157.0,
97229.0,
97320.0,
97391.0,
97501.0,
97604.0,
97682.0,
97742.0,
97811.0,
97900.0,
97962.0,
98016.0,
98080.0,
98176.0]

ESP=[4861883.0,
4871444.0,
4877755.0,
4877755.0,
4877755.0,
4887112.0,
4892640.0,
4898258.0,
4903021.0,
4907461.0,
4907461.0,
4907461.0,
4915265.0,
4918526.0,
4922249.0,
4926324.0,
4929546.0,
4929546.0,
4929546.0,
4935534.0,
4937984.0,
4940824.0,
4943855.0,
4946601.0,
4946601.0,
4946601.0,
4951640.0,
4953930.0,
4956691.0,
4959091.0,
4961128.0,
4961128.0,
4961128.0,
4965399.0,
4967200.0,
4969503.0,
4971310.0,
4973619.0,
4973619.0,
4973619.0,
4977448.0,
4977448.0,
4980206.0,
4982138.0,
4984386.0,
4984386.0,
4984386.0,
4988878.0,
4990767.0,
4993295.0,
4995176.0,
4997732.0,
4997732.0,
4997732.0,
5002217.0,
5004143.0,
5006675.0,
5008887.0,
5011148.0,
5011148.0,
5011148.0,
5011148.0,
5016968.0,
5019255.0,
5022546.0,
5025639.0,
5025639.0,
5025639.0,
5032056.0,
5032056.0,
5038517.0,
5042803.0]

SUE=[1127917.0,
1129131.0,
1130525.0,
1130525.0,
1130525.0,
1130525.0,
1133449.0,
1135160.0,
1136535.0,
1138017.0,
1138017.0,
1138017.0,
1138017.0,
1141673.0,
1142770.0,
1143973.0,
1144982.0,
1144982.0,
1144982.0,
1144982.0,
1146968.0,
1147879.0,
1148641.0,
1149407.0,
1149407.0,
1149407.0,
1149407.0,
1151173.0,
1152027.0,
1152886.0,
1153655.0,
1153655.0,
1153655.0,
1153655.0,
1155534.0,
1156248.0,
1157083.0,
1157822.0,
1157822.0,
1157822.0,
1157822.0,
1159560.0,
1160465.0,
1161264.0,
1161933.0,
1161933.0,
1161933.0,
1161933.0,
1163595.0,
1164402.0,
1165194.0,
1165996.0,
1165996.0,
1165996.0,
1165996.0,
1168271.0,
1169530.0,
1170422.0,
1171512.0,
1171512.0,
1171512.0,
1171512.0,
1174273.0,
1175425.0,
1176269.0,
1177094.0,
1177094.0,
1177094.0,
1177094.0,
1179192.0,
1180518.0,
1181532.0]

TUR=[6412247.0,
6435743.0,
6458600.0,
6478633.0,
6498024.0,
6518986.0,
6542624.0,
6566538.0,
6590384.0,
6613946.0,
6636869.0,
6658221.0,
6682834.0,
6710636.0,
6738860.0,
6766978.0,
6794670.0,
6820831.0,
6847229.0,
6874917.0,
6904255.0,
6932423.0,
6960267.0,
6987464.0,
7013609.0,
7039470.0,
7066658.0,
7095550.0,
7124936.0,
7154040.0,
7182913.0,
7210886.0,
7238237.0,
7267047.0,
7296849.0,
7327317.0,
7357306.0,
7387507.0,
7416152.0,
7444522.0,
7475085.0,
7508945.0,
7540193.0,
7570902.0,
7601596.0,
7630133.0,
7654247.0,
7683487.0,
7714349.0,
7744109.0,
7772574.0,
7800766.0,
7826983.0,
7851775.0,
7879438.0,
7909081.0,
7935977.0,
7961505.0,
7985914.0,
8009010.0,
8032958.0,
8061636.0,
8091432.0,
8121196.0,
8150678.0,
8178871.0,
8206345.0,
8233649.0,
8261473.0,
8290135.0,
8317394.0,
8342292.0]

UKD=[6856933.0,
6894915.0,
6937270.0,
6973995.0,
7010540.0,
7051516.0,
7089051.0,
7127630.0,
7165200.0,
7202212.0,
7231111.0,
7259752.0,
7290168.0,
7316931.0,
7346832.0,
7373451.0,
7406017.0,
7435493.0,
7464791.0,
7500734.0,
7531922.0,
7565751.0,
7601598.0,
7637314.0,
7667290.0,
7700358.0,
7737941.0,
7772788.0,
7808054.0,
7843887.0,
7878571.0,
7908091.0,
7937810.0,
7972312.0,
8005502.0,
8044424.0,
8084322.0,
8119442.0,
8158935.0,
8192589.0,
8232327.0,
8270182.0,
8311851.0,
8356596.0,
8400983.0,
8443882.0,
8488685.0,
8537650.0,
8581278.0,
8630076.0,
8681795.0,
8730787.0,
8775889.0,
8814735.0,
8851104.0,
8894843.0,
8938965.0,
8978443.0,
9021701.0,
9062710.0,
9100442.0,
9140441.0,
9174153.0,
9215683.0,
9252646.0,
9286618.0,
9317072.0,
9346961.0,
9379286.0,
9412185.0,
9451884.0,
9495395.0]

lastTenDay = FRA[-10:]
first10DayALL = ALL[:10]

def corelation_covid(country, country2):
    lenCountry = len(country) + 1
    for i in range(lenCountry - 10):
        matrix = np.corrcoef(lastTenDay, country[:10])
        country.pop(0)
        country2.append(matrix.min())

TAB = [ALL, ISR, ITA, CHI, ESP, UKD, TUR, SUE, RUS, NOR]

ALL2 = []
ISR2 = []
ITA2 = []
CHI2 = []
ESP2 = []
UKD2 = []
TUR2 = []
SUE2 = []
RUS2 = []
NOR2 = []

TAB2 = [ALL2, ISR2, ITA2, CHI2, ESP2, UKD2, TUR2, SUE2, RUS2, NOR2]

bestCoreForEveryCountry = []

for i in range(len(TAB)):
    corelation_covid(TAB[i], TAB2[i])

for countries in TAB2:
    bestCoreForEveryCountry.append(max(countries))

print(bestCoreForEveryCountry)