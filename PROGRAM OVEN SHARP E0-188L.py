# PROGRAM OVEN SHARP EO-18BL PROMAG ULTRA

import time
penentuanbahasa = bool
penentuandurasi = bool
penentuanproses = bool
penentuanstandby = bool
penentuantemperatur = bool
presetorno = bool
timerproses = bool
print("Please select your preferred languange;")
print("1. English")
print("2. Indonesian")
penentuanbahasa = True
while(penentuanbahasa==True):
    inputbahasa = bool
    inputbahasa = True
    while(inputbahasa==True):
        try:
            languange = int(input("Enter Preferred Languange (1 or 2): "))
            if(languange == 1 or 2):
                inputbahasa = False
        except ValueError:
            print("We Don't Understand, Please Select 1 Or 2 As Your Preferred Languange")

    if(languange==2):
        standbymode= False
        penentuanbahasa = False
        print("OVEN PINTAR SHARP EO-118L PROMAG ULTRA")
        print("Silahkan Input Username Sebagai Verifikasi Pengguna")
        Username = str(input("Username: "))
        print(f"Selamat Datang, {Username}")

        presetorno = bool
        makanan = str
        makananlist = [""]*5
        print("Mohon Urutkan 5 Makanan Yang Akan Sering Anda Masukan Ke Smart Oven")
        for i in range(5):
            makananlist[i] = str(input('Makanan Ke-' + str(i + 1) + ': '))

        menggunakanoven = bool
        menggunakanoven = True
        while(menggunakanoven == True):
            presetorno = True
            while(presetorno == True):
                print("Makanan Apa Yang Ingin Kau Proses Hari Ini?")
                print("1. Buka Preset")
                print("2. Makanan Baru")
                print("3. Kembali")
                try:
                    presetmakanan = int(input("Saya Ingin (Ketik Angka 1, 2, atau 3): "))
                    if(presetmakanan == 1):
                        pilihpreset = bool
                        print("Membuka Preset")
                        print(f"1. {makananlist[0]}")
                        print(f"2. {makananlist[1]}")
                        print(f"3. {makananlist[2]}")
                        print(f"4. {makananlist[3]}")
                        print(f"5. {makananlist[4]}")
                        pilihpreset = True
                        while(pilihpreset == True):
                            try:
                                preset = int(input("Saya Ingin Menggunakan Preset (Ketik Angka 1-5): "))
                                if (preset == 1):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[0]
                                    print(f"Baik, Menggunakan Preset {makanan}")
                                elif (preset == 2):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[1]
                                    print(f"Baik, Menggunakan Preset {makanan}")                    
                                elif (preset == 3):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[2]
                                    print(f"Baik, Menggunakan Preset {makanan}")    
                                elif (preset == 4):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[3]
                                    print(f"Baik, Menggunakan Preset {makanan}")             
                                elif (preset == 5):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[4]
                                    print(f"Baik, Menggunakan Preset {makanan}")
                                else:
                                    print("Maaf, Kita Tidak Mempunyai Preset Tersebut")
                            except ValueError:
                                print("Maaf, Tolong Masukan Angka 1, 2, 3, 4, atau 5")
                    elif(presetmakanan == 2):
                        print("Baik, Tolong Masukan Nama/Jenis Makanan Yang Ingin Anda Masak")
                        makanan = str(input("Saya Ingin Memasak: "))
                        presetorno = False
                        penentuanproses = True
                        print(f"Baik, Kita Akan Kita Masak {makanan}")
                    elif(presetmakanan == 3):
                        presetorno = False
                        timerproses = False
                        standbymode = True
                        
                except ValueError:
                    print("Maaf, Tolong Ketik Angka 1 atau 2 Saja Untuk Menentukan Pilihan Anda")        
                                        
            while(penentuanproses==True):
                print("Apa Yang Ingin Anda Lakukan Hari Ini?")
                print("1. Baking")
                print("2. Roasting")
                print("3. Broiling")
                print("4. Dehydration")
                print("5. Reheat")
                inputproses = bool
                inputproses = True
                while(inputproses == True):
                    try:
                        proses = int(input("Saya Ingin (Ketik Angka 1-5): "))
                        if(proses == 1 or 2 or 3 or 4 or 5):
                            inputproses = False
                    except ValueError:
                        print("Maaf, Tolong Masukan Angka 1, 2, 3, 4, Atau 5 Untuk Memilih Proses")
            
                if(proses==1):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Baking"
                    print(f"Baik {Username}, Mengatur Oven Untuk {proses}")
                elif(proses==2):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Roasting"
                    print(f"Baik {Username}, Mengatur Oven Untuk {proses}")
                elif(proses==3):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Broiling"
                    print(f"Baik {Username}, Mengatur Oven Untuk {proses}")
                elif(proses==4):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Dehydration"
                    print(f"Baik {Username}, Mengatur Oven Untuk {proses}")
                elif(proses==5):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Reheat"
                    print(f"Baik {Username}, Mengatur Oven Untuk {proses}")
                else:
                    print("Maaf, Proses Yang Ada Masukan Tidak Valid")

            while(penentuantemperatur==True):
                print(f"Masukan Suhu Untuk {proses}")
                inputtemperatur = bool
                inputtemperatur = True
                while(inputtemperatur == True):
                    try:
                        suhu = int(input("Suhu (Min 50, Max 230): "))
                        if(suhu<=0 or suhu>=0):
                            inputtemperatur = False
                    except ValueError:
                        print("Maaf, Kami Tidak Mengerti Input Yang Anda Masukan, Mohon Masukan Angka Di Antara 50-230")

                if(50<=suhu<=230):
                    penentuantemperatur = False
                    penentuandurasi = True
                    print(f"Baik, Menyetel Suhu Di {suhu} C")
                elif(suhu<50 or 230<suhu):
                    print("Maaf, Suhu Tersebut Diluar Kemampuan Oven Kami")

            while(penentuandurasi== True):
                print(f"Masukan Durasi Untuk Proses {proses}")
                inputdurasi = bool
                inputdurasi = True
                while(inputdurasi == True):
                    try:
                        durasi = int(input("Waktu (Dalam Menit): "))
                        if(durasi<=0 or durasi>= 0):
                            inputdurasi = False
                    except ValueError:
                        print("Maaf, Kami Tidak Mengerti Input Yang Anda Masukan, Mohon Masukan Angka Di Antara 0 dan 1000")

                if(0<durasi<1000):
                    penentuandurasi = False
                    timerproses = True
                    print(f"Baik, Menyetel Durasi Di {durasi} Menit")
                elif(durasi==0 or durasi>=1000):
                    print("Maaf, Durasi Diluar Kemampuan Oven Kami")

            if(standbymode == False):    
                if(proses == "Baking"):
                    kematangan = 185*45
                    tingkatkematangan = float(((durasi*suhu)/(kematangan))*100)
                elif(proses == "Broiling"):
                    kematangan = 225*10
                    tingkatkematangan = float(((durasi*suhu)/(kematangan))*100)
                elif(proses == "Roasting"):
                    kematangan = 205*12
                    tingkatkematangan = float(((durasi*suhu)/(kematangan))*100)

            if(standbymode == False):
                if(80<tingkatkematangan<120):
                    grade = "Matang"
                elif(tingkatkematangan>120):
                    grade = "Gosong"
                elif(tingkatkematangan<80):
                    grade = "Mentah"
        
            def timer(Jam, Menit, Detik):
                totaldetik = Jam*3600 + Menit*60 + Detik
                while(totaldetik > 0):
                    Menit, Detik = divmod(totaldetik, 60)
                    Jam, Menit = divmod(Menit, 60)
                    print(f"\rWaktu Tersisa: {Jam:02d}:{Menit:02d}:{Detik:02d}", end="", flush=True)
                    time.sleep(1)
                    totaldetik -= 1
                print("")
                print(f"Proses {proses} Sudah Selesai")
                if(proses == "Baking" or proses == "Roasting" or proses == "Broiling"):
                    print(f"Tingkat Kematangan {tingkatkematangan}%, {makanan} Anda {grade}")

            if(timerproses == True):
                print(f"Memulai Proses {proses} Untuk {makanan}")
                timer(0, durasi, 0)
            
            while(standbymode == True):
                penentuanstandby = bool
                print("OVEN PINTAR SHARP EO-118L PROMAG ULTRA")
                print("Siap Digunakan Kapan Saja, Pilih Untuk Melanjutkan")
                print("1. Gunakan")
                print("2. Shut Dowm")
                penentuanstandby = True
                while(penentuanstandby == True):
                    try:
                        standby = int(input("(Ketik 1/2): "))
                        if(standby == 1):
                            print(f"Selamat Datang Kembali, {Username}")
                            penentuanstandby = False
                            standbymode = False
                        elif(standby == 2):
                            print(f"Terima Kasih Sudah Menggunakan Oven Kami, {Username}")
                            penentuanstandby = False
                            standbymode = False
                            menggunakanoven = False
                            time.sleep(3)
                            SystemExit
                        else:
                            print("Maaf, Tolong Masukan Angka 1 atau 2")
                    except ValueError:
                        print("Maaf, Tolong Masukan Angka 1 atau 2")

    elif(languange==1):
        standbymode= False
        penentuanbahasa = False
        print("SMART OVEN SHARP EO-118L ULTRA PROMAG")
        print("Please Input Your Username As A Verification Method")
        Username = str(input("Username: "))
        print(f"Good Day, {Username}")

        presetorno = bool
        makanan = str
        makananlist = [""]*5
        print("Please Input 5 Food That You Wish To Save")
        for i in range(5):
            makananlist[i] = str(input('Food Number ' + str(i + 1) + ': '))
        
        menggunakanoven = bool
        menggunakanoven = True
        while(menggunakanoven == True):
            presetorno = True
            while(presetorno == True):
                print("What Kind Of Food Do You Want To Process?")
                print("1. Open Saved Food")
                print("2. New Food")
                print("3. Return")
                try:
                    presetmakanan = int(input("I Want To (Enter Number 1, 2, or 3): "))
                    if(presetmakanan == 1):
                        pilihpreset = bool
                        print("Opening Saved Foods")
                        print(f"1. {makananlist[0]}")
                        print(f"2. {makananlist[1]}")
                        print(f"3. {makananlist[2]}")
                        print(f"4. {makananlist[3]}")
                        print(f"5. {makananlist[4]}")
                        pilihpreset = True
                        while(pilihpreset == True):
                            try:
                                preset = int(input("I Want To Process (Enter Number 1-5): "))
                                if (preset == 1):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[0]
                                    print(f"Understood, Processing {makanan}")
                                elif (preset == 2):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[1]
                                    print(f"Understood, Processing {makanan}")                    
                                elif (preset == 3):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[2]
                                    print(f"Understood, Processing {makanan}")    
                                elif (preset == 4):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[3]
                                    print(f"Understood, Processing {makanan}")             
                                elif (preset == 5):
                                    pilihpreset = False
                                    presetorno = False
                                    penentuanproses = True
                                    makanan = makananlist[4]
                                    print(f"Understood, Processing {makanan}")
                                else:
                                    print("Im Sorry, We Don't Have That Saved")
                            except ValueError:
                                print("Im Sorry, Please Enter Number 1, 2, 3, 4, or 5")
                    elif(presetmakanan == 2):
                        print("Understood, Please Enter What Kind Of Food Do You Want Process")
                        makanan = str(input("I Want To Process: "))
                        presetorno = False
                        penentuanproses = True
                        print(f"Understood, We Will Process {makanan}")
                    elif(presetmakanan == 3):
                        presetorno = False
                        timerproses = False
                        standbymode = True
                        
                except ValueError:
                    print("Im Sorry, Please Enter Number 1 or 2 To Choose")        
                                        
            while(penentuanproses==True):
                print("What Do You Want To Do Today?")
                print("1. Baking")
                print("2. Roasting")
                print("3. Broiling")
                print("4. Dehydration")
                print("5. Reheat")
                inputproses = bool
                inputproses = True
                while(inputproses == True):
                    try:
                        proses = int(input("I Want To (Enter Angka 1-5): "))
                        if(proses == 1 or 2 or 3 or 4 or 5):
                            inputproses = False
                    except ValueError:
                        print("I'm Sorry, Please Enter Number 1, 2, 3, 4, or 5 To Choose")
            
                if(proses==1):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Baking"
                    print(f"Understood {Username}, Setting Oven To {proses}")
                elif(proses==2):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Roasting"
                    print(f"Understood {Username}, Setting Oven To {proses}")
                elif(proses==3):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Broiling"
                    print(f"Understood {Username}, Setting Oven To {proses}")
                elif(proses==4):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Dehydration"
                    print(f"Understood {Username}, Setting Oven To {proses}")
                elif(proses==5):
                    penentuanproses = False
                    penentuantemperatur = True
                    proses = "Reheat"
                    print(f"Understood {Username}, Setting Oven To {proses}")
                else:
                    print("I'm Sorry, The Process You Entered Is Not Valid")

            while(penentuantemperatur==True):
                print(f"Enter Temperature For {proses}")
                inputtemperatur = bool
                inputtemperatur = True
                while(inputtemperatur == True):
                    try:
                        suhu = int(input("Temperature (Min 50, Max 230): "))
                        if(suhu<=0 or suhu>=0):
                            inputtemperatur = False
                    except ValueError:
                        print("I'm Sorry, We Don't Understand Your Input, Please Enter A Number Between 50-230")

                if(50<=suhu<=230):
                    penentuantemperatur = False
                    penentuandurasi = True
                    print(f"Understood, Setting Temperature At {suhu} C")
                elif(suhu<50 or 230<suhu):
                    print("I'm Sorry, That Temperature Is Above Our Oven's Capabilities")

            while(penentuandurasi== True):
                print(f"Enter Duration For {proses}")
                inputdurasi = bool
                inputdurasi = True
                while(inputdurasi == True):
                    try:
                        durasi = int(input("Duration (In Minutes): "))
                        if(durasi<=0 or durasi>= 0):
                            inputdurasi = False
                    except ValueError:
                        print("I'm Sorry, We Don't Understand Your Input, Please Enter A Number Between 0 And 1000")

                if(0<durasi<1000):
                    penentuandurasi = False
                    timerproses = True
                    print(f"Understood, Setting Duration At {durasi} Minutes")
                elif(durasi==0 or durasi>=1000):
                    print("I'm Sorry, That Duration Is Above Our Oven's Capabilities")

            if(standbymode == False):    
                if(proses == "Baking"):
                    kematangan = 185*45
                    tingkatkematangan = float(((durasi*suhu)/(kematangan))*100)
                elif(proses == "Broiling"):
                    kematangan = 225*10
                    tingkatkematangan = float(((durasi*suhu)/(kematangan))*100)
                elif(proses == "Roasting"):
                    kematangan = 205*12
                    tingkatkematangan = float(((durasi*suhu)/(kematangan))*100)

            if(standbymode == False):
                if(80<tingkatkematangan<120):
                    grade = "Cooked"
                elif(tingkatkematangan>120):
                    grade = "Overcooked"
                elif(tingkatkematangan<80):
                    grade = "Raw"
        
            def timer(Jam, Menit, Detik):
                totaldetik = Jam*3600 + Menit*60 + Detik
                while(totaldetik > 0):
                    Menit, Detik = divmod(totaldetik, 60)
                    Jam, Menit = divmod(Menit, 60)
                    print(f"\rTime Left: {Jam:02d}:{Menit:02d}:{Detik:02d}", end="", flush=True)
                    time.sleep(1)
                    totaldetik -= 1
                print("")
                print(f"The {proses} Process Is Done")
                if(proses == "Baking" or proses == "Roasting" or proses == "Broiling"):
                    print(f"Your Food Is {tingkatkematangan}%  Done, Your {makanan} Is {grade}")
                

            if(timerproses == True):
                print(f"Starting {proses} To {makanan}")
                timer(0, durasi, 0)
            
            while(standbymode == True):
                penentuanstandby = bool
                print("SMART OVEN SHARP EO-118L ULTRA PROMAG")
                print("Ready To Use, Choose To Continue")
                print("1. Use")
                print("2. Shut Dowm")
                penentuanstandby = True
                while(penentuanstandby == True):
                    try:
                        standby = int(input("(Enter 1/2): "))
                        if(standby == 1):
                            print(f"Welcome Back, {Username}")
                            penentuanstandby = False
                            standbymode = False
                        elif(standby == 2):
                            print(f"Thank You For Using Our Oven, {Username}")
                            penentuanstandby = False
                            standbymode = False
                            menggunakanoven = False
                            time.sleep(3)
                            SystemExit
                        else:
                            print("I'm Sorry, Please Enter Number 1 or 2")
                    except ValueError:
                        print("I'm Sorry, Please Enter Number 1 or 2")        
    else:
        print("Please Try Again")