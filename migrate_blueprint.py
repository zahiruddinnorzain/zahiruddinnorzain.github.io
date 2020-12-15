import psycopg2
import datetime
import time
import json
from os import system
# import keyboard

# time now
timenow = datetime.datetime.now()

# connect db 2
con2 = psycopg2.connect(
	host = "localhost",
	database = "temp_ssipr",
	user = "admin",
	password = "$admin$",
	)


cur2 = con2.cursor()

# -----------------------------------------------------------------------
# CONFIGURATION
# start id with number, cth agensi_id_seq
# report_name = 'report_role.txt'
# column_name = 'role_user'
# start_id_with = 1
# -------------------------------------------------------------------------

with open('blueprint.json', 'r') as f:
	data = f.read()
	data = data.replace('},]', '}]')

out = json.loads(data)

# total data input
total_data = len(out)
total = 0


# -------------------------------------------------------------------------

# ---------------------------------------------------------------------------

for r in range(len(out)):
# for r in rows:

	# SEND
	if (out[r]["nama_kir"] != None):

		#cleaning
		# if out[r]["tkh_kemaskini"] == '':
		# 	out[r]["tkh_kemaskini"] = str(timenow)

		# if out[r]["tkh_dimasukkan"] == '':
		# 	out[r]["tkh_dimasukkan"] = str(timenow)

		# if out[r]["kaum"] != '':

		# 	if out[r]["kaum"] == 'MELAYU':
		# 		out[r]["kaum"] = 'HARI RAYA AIDILFITRI'

		# 	if out[r]["kaum"] == 'CINA':
		# 		out[r]["kaum"] = 'TAHUN BARU CINA'

		# 	if out[r]["kaum"] == 'INDIA':
		# 		out[r]["kaum"] = 'DEEPAVALI'

		# # a[4]+a[5] for dun
		# # print(out[r]["id_kemasukan"])
		# namadun = out[r]["id_kemasukan"]

		# if out[r]["id_kemasukan"] == 'azizah' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "2" #sabak

		# if out[r]["id_kemasukan"] == 'syanida' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "31"

		# if out[r]["id_kemasukan"] == 'hidayah' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "14"

		# # if out[r]["id_kemasukan"] == 'adun13b' and out[r]["dun_pembayar"] == '':
		# # 	out[r]["id_kemasukan"] = "13"

		# if out[r]["id_kemasukan"] == 'jannati' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "32"

		# if out[r]["id_kemasukan"] == 'hadi' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "44"

		# if out[r]["id_kemasukan"] == 'rhysa' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "10"

		# if out[r]["id_kemasukan"] == 'sofia' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "35"

		# if out[r]["id_kemasukan"] == 'upen5' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "8"

		# if out[r]["id_kemasukan"] == 'izzul' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "17"

		# if out[r]["id_kemasukan"] == 'azreen' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "33"

		# if out[r]["id_kemasukan"] == 'izan' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "44"

		# if out[r]["id_kemasukan"] == 'upen4' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "6"

		# if out[r]["id_kemasukan"] == 'upen3' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "27"

		# if out[r]["id_kemasukan"] == 'upen6' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "20"

		# # if out[r]["id_kemasukan"] == 'adun9c' and out[r]["dun_pembayar"] == '':
		# # 	out[r]["id_kemasukan"] = "9"

		# if (len(namadun) >= 4):
		# 	if (namadun[0]+namadun[1]+namadun[2]+namadun[3]) == 'adun' or (namadun[0]+namadun[1]+namadun[2]+namadun[3]) == 'Adun':
		# 		try:
		# 			cek = int(namadun[4])+int(namadun[5])
		# 			out[r]["id_kemasukan"] = namadun[4]+namadun[5]
		# 		except:
		# 			out[r]["id_kemasukan"] = namadun[4]


		# if out[r]["id_kemasukan"] != '' and out[r]["dun_pembayar"] != '':
		if out[r]["dun"] == "SUNGAI AIR TAWAR":
			out[r]["dun"] = "1"
		elif out[r]["dun"] == "SABAK":
			out[r]["dun"] = "2"
		elif out[r]["dun"] == "SUNGAI PANJANG" or out[r]["dun"] == "SUNGAI PINANG":
			out[r]["dun"] = "3"
		elif out[r]["dun"] == "SEKINCHAN":
			out[r]["dun"] = "4"
		elif out[r]["dun"] == "HULU BERNAM":
			out[r]["dun"] = "5"
		elif out[r]["dun"] == "KUALA KUBU BAHARU":
			out[r]["dun"] = "6"
		elif out[r]["dun"] == "BATANG KALI":
			out[r]["dun"] = "7"
		elif out[r]["dun"] == "SUNGAI BURONG":
			out[r]["dun"] = "8"
		elif out[r]["dun"] == "PERMATANG":
			out[r]["dun"] = "9"
		elif out[r]["dun"] == "BUKIT MELAWATI":
			out[r]["dun"] = "10"
		elif out[r]["dun"] == "IJOK":
			out[r]["dun"] = "11"
		elif out[r]["dun"] == "JERAM":
			out[r]["dun"] = "12"
		elif out[r]["dun"] == "KUANG":
			out[r]["dun"] = "13"
		elif out[r]["dun"] == "RAWANG":
			out[r]["dun"] = "14"
		elif out[r]["dun"] == "TAMAN TEMPLER":
			out[r]["dun"] = "15"
		elif out[r]["dun"] == "SUNGAI TUA" or out[r]["dun"] == "BATU CAVES":
			out[r]["dun"] = "16"
		elif out[r]["dun"] == "GOMBAK SETIA":
			out[r]["dun"] = "17"
		elif out[r]["dun"] == "HULU KELANG":
			out[r]["dun"] = "18"
		elif out[r]["dun"] == "BUKIT ANTARABANGSA":
			out[r]["dun"] = "19"
		elif out[r]["dun"] == "LEMBAH JAYA":
			out[r]["dun"] = "20"
		elif out[r]["dun"] == "PANDAN INDAH":
			out[r]["dun"] = "21"
		elif out[r]["dun"] == "TERATAI":
			out[r]["dun"] = "22"
		elif out[r]["dun"] == "DUSUN TUA" or out[r]["dun"] == "CHEMPAKA" :
			out[r]["dun"] = "23"
		elif out[r]["dun"] == "SEMENYIH":
			out[r]["dun"] = "24"
		elif out[r]["dun"] == "KAJANG":
			out[r]["dun"] = "25"
		elif out[r]["dun"] == "SUNGAI RAMAL":
			out[r]["dun"] = "26"
		elif out[r]["dun"] == "BALAKONG" or out[r]["dun"] == "BANGI":
			out[r]["dun"] = "27"
		elif out[r]["dun"] == "SERI KEMBANGAN":
			out[r]["dun"] = "28"
		elif out[r]["dun"] == "SERI SERDANG":
			out[r]["dun"] = "29"
		elif out[r]["dun"] == "KINRARA":
			out[r]["dun"] = "30"
		elif out[r]["dun"] == "SUBANG JAYA":
			out[r]["dun"] = "31"
		elif out[r]["dun"] == "SERI SETIA":
			out[r]["dun"] = "32"
		elif out[r]["dun"] == "TAMAN MEDAN":
			out[r]["dun"] = "33"
		elif out[r]["dun"] == "BUKIT GASING":
			out[r]["dun"] = "34"
		elif out[r]["dun"] == "KAMPUNG TUNKU":
			out[r]["dun"] = "35"
		elif out[r]["dun"] == "BANDAR UTAMA" or  out[r]["dun"] == "DAMANSARA UTAMA" :
			out[r]["dun"] = "36"
		elif out[r]["dun"] == "BUKIT LANJAN":
			out[r]["dun"] = "37"
		elif out[r]["dun"] == "PAYA JARAS":
			out[r]["dun"] = "38"
		elif out[r]["dun"] == "KOTA DAMANSARA":
			out[r]["dun"] = "39"
		elif out[r]["dun"] == "KOTA ANGGERIK" or out[r]["dun"] == "KOTA ALAM SHAH":
			out[r]["dun"] = "40"
		elif out[r]["dun"] == "BATU TIGA":
			out[r]["dun"] = "41"
		elif out[r]["dun"] == "MERU":
			out[r]["dun"] = "42"
		elif out[r]["dun"] == "SEMENTA":
			out[r]["dun"] = "43"
		elif out[r]["dun"] == "SELAT KLANG":
			out[r]["dun"] = "44"
		elif out[r]["dun"] == "BANDAR BARU KLANG":
			out[r]["dun"] = "45"
		elif out[r]["dun"] == "PELABUHAN KLANG":
			out[r]["dun"] = "46"
		elif out[r]["dun"] == "PANDAMARAN":
			out[r]["dun"] = "47"
		elif out[r]["dun"] == "SENTOSA" or out[r]["dun"] == "SERI ANDALAS":
			out[r]["dun"] = "48"
		elif out[r]["dun"] == "SUNGAI KANDIS":
			out[r]["dun"] = "49"
		elif out[r]["dun"] == "KOTA KEMUNING" or  out[r]["dun"] == "SERI MUDA" :
			out[r]["dun"] = "50"
		elif out[r]["dun"] == "SIJANGKANG":
			out[r]["dun"] = "51"
		elif out[r]["dun"] == "BANTING" or out[r]["dun"] == "TELUK DATUK":
			out[r]["dun"] = "52"
		elif out[r]["dun"] == "MORIB":
			out[r]["dun"] = "53"
		elif out[r]["dun"] == "TANJUNG SEPAT" or out[r]["dun"] == "TANJONG SEPAT": 
			out[r]["dun"] = "54"
		elif out[r]["dun"] == "DENGKIL":
			out[r]["dun"] = "55"
		elif out[r]["dun"] == "SUNGAI PELEK":
			out[r]["dun"] = "56"
		elif out[r]["dun"] == "":
			out[r]["dun"] = "0"
		elif out[r]["dun"] == "" or out[r]["dun"] == "Sila Pilih" :
			out[r]["dun"] = "0"
			# elif out[r]["id_kemasukan"] != 'ana':
			# 	id_kemasukan_tmp = out[r]["id_kemasukan"]
			# 	id_kemasukan_tmp = id_kemasukan_tmp[4]+id_kemasukan_tmp[5]
			# 	out[r]["id_kemasukan"] = int(id_kemasukan_tmp)

		number = out[r]["pendapatan_keseluruhan"]
		number = int(number)
		out[r]["pendapatan_keseluruhan"] = number
		# print(number)


		# try:
		cur2.execute(
						"""INSERT INTO permohonan_blueprint (
						id, 
						name,
						ic_pemohon,
						daerah,
						no_tel,
						no_tel_rumah,
						jumlah_pendapatan_isi_rumah,
						dun)
						VALUES 
						(%s, %s, %s, %s, %s, %s, %s, %s)""", 
						(
							out[r]["main_index"], 
							out[r]["nama_kir"], 
							out[r]["no_kp_baru_kir"], 
							out[r]["daerah"], 
							out[r]["no_hp"], 
							out[r]["no_telefon"], 
							out[r]["dun"], 
							out[r]["pendapatan_keseluruhan"], 
						)
					)
		# print(out[r]["nama_kir"] + " = OK", )
		total = total+1

		# Print status every 500 addresses
		if total % 500 == 0:
			print("Completed {} of {} data".format( total, len(out) ))

		# if keyboard.is_pressed('s'):
			# print('exiting..')
			# # close
			# cur2.close()
			# con2.close()
			# exit()

		# percent = float((total/total_data)*100)
		# print(str(round(percent, 3))+' %')
		# system('clear')



		# write report
		# with open(report_name, 'a') as the_file:
		# 	the_file.write(f"{r[3]} = OK\n")
		# except:
			# print("except ERROR")


	else:
		# print(f"{out[r]["no_kp"]} = ERROR\n")
		# print(out[r]["no_kp"])
		# total_error += 1
		print("ERROR")

		# write report
		# with open(report_name, 'a') as the_file:
		# 	the_file.write(f"{r[0]} = ERROR\n")

	# time.sleep(0.01)


# ---------------------------------------------------------------------------

cur2.execute("SELECT * FROM permohonan_blueprint")

# save data to db
# con2.commit()

# fetch all
rows2 = cur2.fetchall()

# output
# for r in rows2:
# 	print (r)
# 	print ('\n')
	# print (r[0])

# show done_migrate
# print(done_migrate)
# print('\n')

# # show total ERROR
# print(f'\nTotal ERROR = {total_error}\n')
# print(f'Total SKIP = {total_skip}\n')
# # write report
# with open(report_name, 'a') as the_file:
# 	the_file.write(f'\nTotal ERROR = {total_error}\n')
# 	the_file.write(f'Total SKIP = {total_skip}\n')
print("TOTAL DATA = " + str(total_data))
print("TOTAL DATA MIGRATE = " + str(total))

# close cursor
cur2.close()

# close connection
con2.close()
