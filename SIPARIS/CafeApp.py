def cafelerAndMenu():
    # ilçelerdeki kafeleri ucuz ve pahalı olarak dictionary de tanımladık.
    global karakoy
    global maltepe
    global kadikoy

    karakoy = {"UCUZ": "Gran Karaköy", "UCUZ2": "Lol Coffee", "UCUZ3": "Books And Coffee", "UCUZ4": "Wood Karaköy",
                   "UCUZ5": "Dem Karaköy",
                   "PAHALI": "Han Karaköy", "PAHALI2": "Coffee Sapiens", "PAHALI3": "Brew Coffeeworks", "PAHALI4": "Funk",
                   "PAHALI5": "Unter", "PAHALI6": "Filbooks"}
    maltepe = {"UCUZ": "Mi Coffees", "UCUZ2": "Kahve Dünyası", "UCUZ3": "Penguen_Coffe", "UCUZ4": "T'chibo",
                   "UCUZ5": "Big Carmeleos Coffee",
                   "PAHALI": "Starbucks", "PAHALI2": "Espressolab", "PAHALI3": "Midpoint", "PAHALI4": "Statement Cafe",
                   "PAHALI5": "Bisquitte"}
    kadikoy = {"UCUZ": "Cocca", "UCUZ2": "Geçmiş Kafe", "UCUZ3": "Deli No. 14", "UCUZ4": "Leman Kültür",
                   "UCUZ5": "Moda Çikolatacısı",
                   "PAHALI": "Doz Roastery", "PAHALI2": "Mortag Coffee", "PAHALI3": "Hale Jale Bütün Mahalle",
                   "PAHALI4": "Coffee Manifesto", "PAHALI5": "Gaf"}

    global konum
    # kafelerin konumlarını, "konum" adını verdiğimiz dictionary'de cafelere eşitledik.
    konum = {"Gran Karaköy": "Kemankeş Karamustafa Paşa, Odun Meydanı Sk. no:2/b, 34425 Beyoğlu/İstanbul",
             "Lol Coffee": "Kemankeş Karamustafa Paşa, Kılıç Ali Paşa Mescidi Sokak, Karaköy No:8, 34425 Beyoğlu/İstanbul",
             "Books And Coffee": "Azapkapı, Teğmen Hüseyin Sofu Sk. No:13, 34431 Beyoğlu/İstanbul",
             "Wood Karaköy": "Kemankeş Karamustafa Paşa, K, Kılıç Ali Paşa Mescidi Sk. No:26, 34425 Beyoğlu/İstanbul",
             "Dem Karaköy": "Arap Cami Mah. Söğüt Sok. No: 1 Eski Posta Han, 34421 Beyoğlu/İstanbul",
             "Han Karaköy": "Kemankeş Karamustafa Paşa, Hoca Tahsin Sk. No:17, 34425 Beyoğlu/İstanbul",
             "Coffee Sapiens": "Kemankeş Karamustafa Paşa, Kılıç Ali Paşa Mescidi Sk. No:10 D:C, 34425 Beyoğlu/İstanbul",
             "Brew Coffeeeworks": "Hobyar, Hamidiye Cd. No:60, 34112 Fatih/İstanbul",
             "Funk": "Kemankeş Karamustafa Paşa, Yuva Sk. no:4/B, 34425 Beyoğlu/İstanbul",
             "Unter": "Kemankeş Karamustafa Paşa, 4 Necatibey Caddesi &, Karaali Kaptan Sk., 34425 Beyoğlu/İstanbul",
             "Mi Coffees": "Altayçeşme, Samanyolu Sk. No:19, 34843 Maltepe/İstanbul",
             "Kahve Dünyası": "Aydınevler, Başıbüyük-Samandıra Yolu No:2007, 34854 Maltepe/İstanbul",
             "Penguen_Coffe": "Yalı Mahallesi, Turgut Özal Bulvarı, No:201/B, Maltepe, İstanbul",
             "T'chibo": "Cevizli, Tugay Yolu Cd. No:73, 34846 Maltepe/İstanbul",
             "Big Carmeleos Coffee": "Cevizli, Tugay Yolu Cd. No:71, 34846 Maltepe/İstanbul",
             "Starbucks": "Yalı Turgut Özal Bulvarı Yaylada AVM No:514, 34840 Maltepe/İstanbul",
             "Espressolab": "Cevizli, Tugay Yolu Cd. No:69 D:C Blok, 34846 Maltepe/İstanbul",
             "Midpoint": "Cevizli, Tugay Yolu Cd. 69-C, 34846 Maltepe/İstanbul",
             "Statement Cafe": "CEVİZLİ ZUHAL CD. GEÇİM İSTANBUL AVM NO:46/C BLOK:B NO:177, 34010 MALTEPE/İstanbul",
             "Bisquitte": "Cevizli, Tugay Yolu Cd. No:69, 34846 Maltepe/İstanbul",
             "Cocca": "Yalı, Rıhtım Cd. No:17, 34844 Maltepe/İstanbul",
             "Geçmiş Kafe": "Osmanağa, Yoğurtçu Şükrü Sk. No: 48, 34734 Kadıköy/İstanbul",
             "Deli No. 14": "Caferağa, Arayıcıbaşı Sk. 10/A, 34710 Kadıköy/İstanbul",
             "Leman Kültür": "Caferağa, Neşet Ömer Sk. No:9, 34710 Kadıköy/İstanbul",
             "Moda Çikolatacısı": "Caferağa, General Asım Gündüz Cd. No81/24 D:No:81/24, 34710 Kadıköy/İstanbul",
             "Doz Roastery": "Caferağa, Ressam Şeref Akdik Sokağı No:19, 34710 Kadıköy/İstanbul",
             "Mortag Coffee": "Caferağa Mah, Muvakkıthane Cd. No:16/A D:Kat:1, 34710, 34710 Kadıköy/İstanbul",
             "Hale Jale Bütün Mahalle": "Caferağa Mahallesi Moda Caddesi & Damacı Sokak Dama Apt. 3/A, 34710 Kadıköy/İstanbul",
             "Coffee Manifesto": "Caferağa, Güneşli Bahçe Sok No:40A, 34710 Kadıköy/İstanbul",
             "Gaf": "Caferağa, Fırıldak Sk. NO:14/D, 34710 Kadıköy/İstanbul"}

    # Dictionary kullanarak her kafenin kendi menüsündeki içecek isimlerini ve fiyatlarını eşitledik.
    global Cocca
    Cocca = {"Espresso": 10, "Americano": 12, "Cortado": 14, "Flat White": 14, "Latte": 14, "Cappucino": 14,
             "Batch Rew Coffee": 12, "Türk Kahvesi": 8, "Affogato": 15, "Çay": 4, "Soda": 4, "Su": 3}

    global Geçmiş_Kafe
    Geçmiş_Kafe = {"Ice Mocha": 13, "Cold Brew": 15, "Japanese Ice Flitter": 14, "Bisqui": 14, "Flitre Kahve": 11,
                   "Hario V60": 13, "Chemex": 13, "Aeropres": 14, "Syphon": 15, "Ristretto": 6,
                   "Espresso (single)": 7, "Espresso Macchiato": 9, "Espresso Con Panna": 10, "Wiener Melange": 11,
                   "Cortado": 12, "Flat White": 11, "Marocchino Caldo": 12, "Cappuccino": 12, "Americano": 11,
                   "Cafe Latte": 12}

    global Deli_No_14
    Deli_No_14 = {"Ice Mocha": 15, "Flitre Kahve": 13, "Espresso ": 8,
                  "Espresso Macchiato": 10, "Cortado": 11, "Cappuccino": 13, "Americano": 11, "Latte": 12,
                  "Flat White": 13,
                  "Türk Kahvesi": 8, "Double Espresso": 10, "Iced Americano": 13, "Red Eye": 13,
                  "Black Eye": 15,
                  "Filtre Kahve V60": 13, "Filtre Kahve": 10}

    global leman_kültür
    leman_kültür = {"Ice Karamel Latte": 15, "Ice Americano": 15, "Flitre Kahve": 12, "Espresso": 10,
                    "Cappucino": 13,
                    "Granül Kahve Sade": 11, "Americano": 13, "Cafe Latte": 14, "Türk Kahvesi": 11,
                    "Double Espresso": 12, "Sakızlı Türk Kahvesi": 12, "Kavunlu Türk Kahvesi": 12,
                    "White Chocolate Mocha": 13, "Machiato": 12, "Granül Kahve Sütlü": 12}

    global Moda_Çikolatacısı
    Moda_Çikolatacısı = {"Flitre Kahve": 12, "Espresso": 9,
                         "Cappuccino": 15, "Americano": 14, "Latte": 15, "Türk Kahvesi": 9,
                         "Double Espresso": 13, "Filtre Kahve": 12, "Sütlü Türk Kahvesi": 10,
                         "Double Türk Kahvesi": 15, "Double Sütlü Türk Kahvesi": 15}

    global Doz_Roastery
    Doz_Roastery = {"Ice Cafe Latte": 18, "Espresso": 15, "Cortado": 16,
                    "Cappuccino": 17, "Americano": 15, "Cafe Latte": 17, "Flat White": 15, "Türk Kahvesi": 15,
                    "Espresso Con Panna": 16, "Iced Americano": 16, "Risretto": 15,
                    "Lungo": 15, "Almond Cortado": 16, "Cafe Miel": 19, "Sonya Latte": 20, "Pumpkin Latte": 18,
                    "Lavander Latte": 18, "Belgeum Latte": 18}

    global Mortag_Coffee
    Mortag_Coffee = {"Pumpkin Latte": 19, "Ginger Pepper Latte": 19, "Dirty Chai Latte": 19,
                     "After Eight Cortado": 18, "Orange Mocha": 20, "Hario V60 Demleme Kahve": 18,
                     "Filtre Kahve": 15, "Espresso": 15, "Americano": 16, "Latte": 18, "Mocha": 20,
                     "Cortado": 16, "Cold Brew": 17, "Iced Latte": 18, "Iced Mocha": 20, "Türk Kahvesi": 17}

    global Hale_Jale_Bütünmahalle
    Hale_Jale_Bütünmahalle = {"Sütlü Kahve": 15, "Türk Kahvesi": 15, "Cappuccino": 16, "Americano": 15,
                              "Latte": 17,
                              "Filtre Kahve": 15, "Moka": 18, "Makiato": 15, "Iced Americano": 16,
                              "Iced Latte": 17,
                              "Fredo": 15, "Greek Frappe": 17, "Double Espresso": 15}

    global Coffe_Manifesto
    Coffe_Manifesto = {"Türk Kahvesi": 15, "Cappuccino": 15, "Americano": 15, "Latte": 15,
                       "Filtre Kahve": 15, "Makiato": 15, "Iced Latte": 18, "Double Espresso": 15,
                       "Flat White": 16,
                       "Cortado": 15, "Affogato": 18, "Ristretto": 15, "Chemex": 18, "Brew V60": 18,
                       "Cold Brew": 18}

    global Gaf_Kafe
    Gaf_Kafe = {"Macchiato": 15, "Caramel Macchiato": 15, "Americano": 15, "Filtre Kahve": 15,
                "Cappucinho": 15,
                "Caramel Latte": 16, "Cafe Mocha": 15, "Flat white": 15, "Winter Coffe": 19,
                "Coffee Miel": 17, "Cortado": 15, "Türk Kahvesi": 15, "Affogato": 16}

    global Mi_Coffees
    Mi_Coffees = {"Zebra Chocolate Mocha": 15, "White Chocolate Mocha": 15, "Honey Cinnamon Latte": 15,
                  "Single Machiato": 11,
                  "Filtre Kahve": 12, "Espresso": 9, "Americano": 13, "Latte": 14, "Mocha": 15,
                  "Frappe": 15, "Greek Frappe": 14, "Oreo Frappe": 15, "Soğuk Sütlü Filtre Kahve": 14,
                  "Cortado": 15, "Single Machiatoo": 11, "Iced Latte": 14, "Iced Mocha": 16, "Türk Kahvesi": 10,
                  "Double Türk Kahvesi": 15}

    global Kahve_Dünyası
    Kahve_Dünyası = {"Espresso": 9, "Espresso Con Panna": 11, "Macchiato": 10, "Double Espresso": 11,
                     "Americano": 12, "Karamelli Machiato": 15,
                     "Lungo Espresso": 13, "Türk Kahvesi": 9, "Damla sakızlı türk Kahvesi": 10, "Mocha": 15,
                     "Double Türk Kahvesi": 10, "Filitre Kahve": 9,
                     "Cafe Latte": 13, "Flat White": 14, "Ristretto": 11, "Kosta Rika": 14, "Kenya": 14,
                     "Kahveli Sıcak Çikolata": 15,
                     "Soğuk Türk Kahvesi": 15, "Cold Brew": 15, "Buzlu Americano": 13, "Buzlu Mocha": 15,
                     "Karamel Frappe": 15, "Çilekli Frappe": 15}

    global Penguen_Coffe
    Penguen_Coffe = {"Iced Latte": 10, "Iced Americano": 15, "Ice Zebra Mocha": 15, "Ice Espresso": 14,
                     "Ice Macchiato": 15, "Ice Chai Latte": 15,
                     "Iced Chilli Mocha": 13, "Turkish Coffe": 10, "Espresso Lungo": 12, "Doppio": 9,
                     "Cortado": 13, "Flat White": 14,
                     "Zebra Mocha": 12, "Red Eye": 15, "Cafe Miel": 15, "Vanilla Frappe": 15,
                     "Mocha Frappe": 14, "White Chocolate Frappe": 15}

    global Tchibo
    Tchibo = {"Filtre Kahve (küçük)": 7, "Filtre kahve (büyük)": 9, "Espresso": 7, "Americano": 11,
              "Latte": 12, "Cappucino": 12,
              "Melange": 12, "Latte Macchiato": 15, "Mocha": 13, "Türk Kahvesi": 8, "Flat White": 12,
              "Cortado": 10,
              "Chai Tea Latte": 12, "Cold Brew": 13, "Cold Brew Latte": 13, "Espresso Shakerato": 11,
              "Mocha Coco Latte": 14,
              "Frappe": 14, "Ice Cocco Latte": 14, "Iced Bannana Latte": 14, "Dalgona": 15}

    global Big_Carmeleos
    Big_Carmeleos = {"Filtre Kahve (küçük)": 8, "Filtre kahve (büyük)": 10, "Espresso": 6, "Americano": 12,
                     "Latte": 13, "Cappucino": 12,
                     "Melange": 13, "Latte Macchiato": 14, "Mocha": 13, "Türk Kahvesi": 7, "Flat White": 11,
                     "Cortado": 12,
                     "Chai Tea Latte": 13, "Cold Brew": 14, "Cold Brew Latte": 15, "Espresso Shakerato": 10,
                     "Mocha Coco Latte": 15,
                     "Frappe": 13, "Ice Cocco Latte": 15, "Iced Bannana Latte": 13, "Dalgona": 15}

    global Starbucks
    Starbucks = {"Macchiato": 16, "Caramel Macchiato": 17, "Americano": 18, "Filtre Kahve": 15,
                 "Cappucinho": 16,
                 "Caramel Latte": 17, "Cafe Mocha": 17, "Flat white": 18, "Winter Coffe": 17,
                 "Coffee Miel": 19, "Cortado": 19, "Türk Kahvesi": 15, "Affogato": 19,
                 "Iced Lattee": 10, "Iced Latte": 15, "Iced Americano": 19, "Ice Zebra Mocha": 20,
                 "Ice Espresso": 16, "Ice Macchiato": 16, "Ice Chai Latte": 15}

    global Espressolab
    Espressolab = {"Türk Kahvesi": 16, "Cappuccino": 16, "Americano": 17, "Latte": 15,
                   "Filtre Kahve": 16, "Makiato": 17, "Iced Latte": 19, "Double Espresso": 16,
                   "Flat White": 17,
                   "Cortado": 18, "Affogato": 19, "Ristretto": 19, "Chemex": 19, "Brew V60": 17,
                   "Cold Brew": 17, "Iced Americano": 20, "Ice Zebra Mocha": 20, "Ice Espresso": 17,
                   "Ice Macchiato": 18}

    global Midpoint
    Midpoint = {"Filtre Kahve": 15, "Espresso": 15, "Americano": 16, "Latte": 15, "Cappucino": 16,
                "Melange": 17, "Latte Macchiato": 17, "Mocha": 15, "Türk Kahvesi": 15, "Flat White": 18,
                "Cortado": 19,
                "Chai Tea Latte": 15, "Cold Brew": 15, "Cold Brew Latte": 15, "Espresso Shakerato": 15,
                "Mocha Coco Latte": 19,
                "Frappe": 16, "Ice Cocco Latte": 17, "Iced Bannana Latte": 16, "Dalgona": 18}

    global Statement_Cafe
    Statement_Cafe = {"Espresso": 15, "Espresso Con Panna": 16, "Macchiato": 15, "Double Espresso": 16,
                      "Americano": 17, "Karamelli Machiato": 17,
                      "Lungo Espresso": 16, "Türk Kahvesi": 15, "Damla sakızlı türk Kahvesi": 16, "Mocha": 15,
                      "Double Türk Kahvesi": 18, "Filitre Kahve": 15,
                      "Cafe Latte": 17, "Flat White": 18, "Ristretto": 19, "Kosta Rika": 16, "Kenya": 16,
                      "Kahveli Sıcak Çikolata": 15,
                      "Soğuk Türk Kahvesi": 15, "Cold Brew": 15, "Buzlu Americano": 17, "Buzlu Mocha": 18,
                      "Karamel Frappe": 16, "Çilekli Frappe": 17}

    global Bisquitte
    Bisquitte = {"Pumpkin Latte": 19, "Ginger Pepper Latte": 19, "Dirty Chai Latte": 19,
                 "After Eight Cortado": 18, "Orange Mocha": 20, "Hario V60 Demleme Kahve:": 18,
                 "Filtre Kahve": 15, "Espresso": 15, "Americano": 16, "Latte": 18, "Mocha": 20,
                 "Cortado": 16, "Cold Brew": 17, "Iced Latte": 18, "Iced Mocha": 20, "Türk Kahvesi": 17}

    global Gran_Karaköy
    Gran_Karaköy = {"Filtre Kahve (küçük)": 10, "Filtre kahve (büyük)": 11, "Espresso": 13, "Americano": 12,
                    "Latte": 14, "Cappucino": 14,
                    "Melange": 12, "Latte Macchiato": 12, "Mocha": 11, "Türk Kahvesi": 8, "Flat White": 14,
                    "Cortado": 15,
                    "Chai Tea Latte": 15, "Cold Brew": 14, "Cold Brew Latte": 14, "Espresso Shakerato": 15,
                    "Mocha Coco Latte": 15,
                    "Frappe": 13, "Ice Cocco Latte": 13, "Iced Bannana Latte": 13, "Dalgona": 13}

    global Lol_Coffee
    Lol_Coffee = {"Ice Cafe Latte": 15, "Espresso": 13, "Cortado": 12,
                  "Cappuccino": 15, "Americano": 15, "Cafe Latte": 15, "Flat White": 15, "Türk Kahvesi": 15,
                  "Espresso Con Panna": 13, "Iced Americano": 13, "Risretto": 13,
                  "Lungo": 13, "Almond Cortado": 15, "Cafe Miel": 14, "Sonya Latte": 15, "Pumpkin Latte": 13,
                  "Lavander Latte": 12, "Belgeum Latte": 13}

    global Books_And_Coffe
    Books_And_Coffe = {"Zebra Chocolate Mocha": 15, "White Chocolate Mocha": 15, "Honey Cinnamon Latte": 15,
                       "Single Machiatoo": 16,
                       "Filtre Kahve": 12, "Espresso": 9, "Americano": 13, "Latte": 14, "Mocha": 15,
                       "Frappe": 15, "Greek Frappe": 14, "Oreo Frappe": 15, "Soğuk Sütlü Filtre Kahve": 14,
                       "Cortado": 15, "Single Machiato": 11, "Iced Latte": 14, "Iced Mocha": 16,
                       "Türk Kahvesi": 10, "Double Türk Kahvesi": 15}

    global Wood_Karaköy
    Wood_Karaköy = {"Macchiato": 13, "Caramel Macchiato": 14, "Americano": 15, "Filtre Kahve": 15,
                    "Cappucinho": 15,
                    "Caramel Latte": 15, "Cafe Mocha": 14, "Flat white": 14, "Winter Coffe": 14,
                    "Coffee Miel": 15, "Cortado": 15, "Türk Kahvesi": 8, "Affogato": 12,
                    "Iced Latte": 10, "Iced Lattee": 15, "Iced Americano": 14, "Ice Zebra Mocha": 13,
                    "Ice Espresso": 15, "Ice Macchiato": 13, "Ice Chai Latte": 15}

    global Dem_Karaköy
    Dem_Karaköy = {"Filtre Kahve (küçük)": 7, "Filtre kahve (büyük)": 9, "Espresso": 7, "Americano": 11,
                   "Latte": 12, "Cappucino": 12,
                   "Melange": 12, "Latte Macchiato": 15, "Mocha": 13, "Türk Kahvesi": 8, "Flat White": 12,
                   "Cortado": 10,
                   "Chai Tea Latte": 12, "Cold Brew": 13, "Cold Brew Latte": 13, "Espresso Shakerato": 11,
                   "Mocha Coco Latte": 14,
                   "Frappe": 14, "Ice Cocco Latte": 14, "Iced Bannana Latte": 14, "Dalgona": 15}

    global Filbooks
    Filbooks = {"Pumpkin Latte": 19, "Ginger Pepper Latte": 19, "Dirty Chai Latte": 19,
                "After Eight Cortado": 18, "Orange Mocha": 20, "Hario V60 Demleme Kahve": 18,
                "Filtre Kahve": 15, "Espresso": 15, "Americano": 16, "Latte": 18, "Mocha": 20,
                "Cortado": 16, "Cold Brew": 17, "Iced Latte": 18, "Iced Mocha": 20, "Türk Kahvesi": 17}

    global Han_Karaköy
    Han_Karaköy = {"Espresso": 15, "Espresso Con Panna": 16, "Macchiato": 15, "Double Espresso": 16,
                   "Americano": 17, "Karamelli Machiato": 17,
                   "Lungo Espresso": 16, "Türk Kahvesi": 15, "Damla sakızlı türk Kahvesi": 16, "Mocha": 15,
                   "Double Türk Kahvesi": 18, "Filitre Kahve": 15,
                   "Cafe Latte": 17, "Flat White": 18, "Ristretto": 19, "Kosta Rika": 16, "Kenya": 16,
                   "Kahveli Sıcak Çikolata": 15,
                   "Soğuk Türk Kahvesi": 15, "Cold Brew": 15, "Buzlu Americano": 17, "Buzlu Mocha": 18,
                   "Karamel Frappe": 16, "Çilekli Frappe": 17}

    global Coffe_Sapiens
    Coffe_Sapiens = {"Filtre Kahve": 15, "Espresso": 15, "Americano": 16, "Latte": 15, "Cappucino": 16,
                     "Melange": 17, "Latte Macchiato": 17, "Mocha": 15, "Türk Kahvesi": 15, "Flat White": 18,
                     "Cortado": 19,
                     "Chai Tea Latte": 15, "Cold Brew": 15, "Cold Brew Latte": 15, "Espresso Shakerato": 15,
                     "Mocha Coco Latte": 19,
                     "Frappe": 16, "Ice Cocco Latte": 17, "Iced Bannana Latte": 16, "Dalgona": 18}

    global Brew_Coffeeworks
    Brew_Coffeeworks = {"Ice Cafe Latte": 18, "Espresso": 15, "Cortado": 16,
                        "Cappuccino": 17, "Americano": 15, "Cafe Latte": 17, "Flat White": 15,
                        "Türk Kahvesi": 15,
                        "Espresso Con Panna": 16, "Iced Americano": 16, "Risretto": 15,
                        "Lungo": 15, "Almond Cortado": 16, "Cafe Miel": 19, "Sonya Latte": 20,
                        "Pumpkin Latte": 18,
                        "Lavander Latte": 18, "Belgeum Latte": 18}

    global Funk
    Funk = {"Ice Cafe Latte": 15, "Espresso": 16, "Cortado": 15,
            "Cappuccino": 15, "Americano": 16, "Cafe Latte": 17, "Flat White": 18, "Türk Kahvesi": 15,
            "Espresso Con Panna": 15, "Iced Americano": 17, "Risretto": 16,
            "Lungo": 15, "Almond Cortado": 18, "Cafe Miel": 15, "Sonya Latte": 15, "Pumpkin Latte": 17,
            "Lavander Latte": 18, "Belgeum Latte": 18}

    global Unter
    Unter = {"Ice Cafe Latte": 16, "Espresso": 15, "Cortado": 15,
             "Cappuccino": 16, "Americano": 15, "Cafe Latte": 15, "Flat White": 16, "Türk Kahvesi": 15,
             "Espresso Con Panna": 17, "Iced Americano": 18, "Risretto": 19,
             "Lungo": 15, "Almond Cortado": 17, "Cafe Miel": 18, "Sonya Latte": 15, "Pumpkin Latte": 19,
             "Lavander Latte": 20, "Belgeum Latte": 20}

    # kafe adını verdiğimiz listenin içine kafe isimlerini yazdık.
    global cafe
    cafe = ["Cocca", "Mi Coffees", "Kahve Dünyası", "Penguen_Coffe", "T'chibo", "Big Carmeleos Coffee", "Starbucks",
            "Espressolab", "Midpoint", "Statement Cafe", "Bisquitte", "Geçmiş Kafe", "Deli No. 14", "Leman Kültür",
            "Moda Çikolatacısı",
            "Doz Roastery", "Mortag Coffee", "Hale Jale Bütün Mahalle", "Coffee Manifesto", "Gaf", "Gran Karaköy",
            "Lol Coffee", "Books And Coffee", "Wood Karaköy", "Dem Karaköy", "Han Karaköy", "Coffee Sapiens",
            "Brew Coffeeworks", "Funk", "Unter", "Filbooks"]

    # menu adını verdiğimiz dictionary nin içinde kafe isimlerinin karşılığına o kafenin menu dictionary sini eşitledik.
    global menu
    menu = {"Cocca": Cocca, "Geçmiş Kafe": Geçmiş_Kafe, "Deli No. 14": Deli_No_14, "Leman Kültür": leman_kültür,
            "Moda Çikolatacısı": Moda_Çikolatacısı, "Doz Roastery": Doz_Roastery, "Mortag Coffee": Mortag_Coffee,
            "Hale Jale Bütün Mahelle": Hale_Jale_Bütünmahalle,
            "Coffee Manifesto": Coffe_Manifesto, "Gaf": Gaf_Kafe, "Gran Karaköy": Gran_Karaköy,
            "Lol Coffee": Lol_Coffee, "Books And Coffee": Books_And_Coffe, "Wood Karaköy": Wood_Karaköy,
            "Dem Karaköy": Dem_Karaköy, "Han Karaköy": Han_Karaköy,
            "Coffee Sapiens": Coffe_Sapiens, "Brew Coffeeworks": Brew_Coffeeworks, "Funk": Funk, "Unter": Unter,
            "Mi Coffees": Mi_Coffees, "Kahve Dünyası": Kahve_Dünyası, "Penguen_Coffe": Penguen_Coffe,
            "T'chibo": Tchibo, "Big Carmeleos": Big_Carmeleos,
            "Starbucks": Starbucks, "Espressolab": Espressolab, "Midpoint": Midpoint, "Statement Cafe": Statement_Cafe,
            "Bisquitte": Bisquitte, "Filbooks": Filbooks}

def para_konum_bilgisi():
    cafemoney = {"karaköy": karakoy, "maltepe": maltepe, "kadıköy": kadikoy}
    iller = ["karaköy", "maltepe", "kadıköy"]

    a = 1  # Burda döngümüzü sağlamak için bi değişken tanıplayıp içine değer atadık.
    while a == 1:  # Doğru para girilebilmesi için döngümüzü kurduk.

        para_bilgisi = int(input("Para Miktarınızı giriniz:"))  # Para bilgisini istedik.
        konum_bilgisi = input("Konum bilgisi giriniz:")  # Konum bilgisini istedik.

        if 0 < para_bilgisi <= 15 and konum_bilgisi in iller:  # Girdiği paraya göre hangi bölgeye ait ona bakıyoruz.
            print(cafemoney[konum_bilgisi]["UCUZ"])
            print(cafemoney[konum_bilgisi]["UCUZ2"])
            print(cafemoney[konum_bilgisi]["UCUZ3"])
            print(cafemoney[konum_bilgisi]["UCUZ4"])
            print(cafemoney[konum_bilgisi]["UCUZ5"])
            a = 2  # Döngüden çıkması için a'yı 2 yapıyoruz.

        elif 15 < para_bilgisi <= 35 and konum_bilgisi in iller:  # Girdiği paraya göre hangi bölgeye ait ona bakıyoruz.
            print(cafemoney[konum_bilgisi]["PAHALI"])
            print(cafemoney[konum_bilgisi]["PAHALI2"])
            print(cafemoney[konum_bilgisi]["PAHALI3"])
            print(cafemoney[konum_bilgisi]["PAHALI4"])
            print(cafemoney[konum_bilgisi]["PAHALI5"])
            a = 2  # Döngüden çıkması için a'yı 2 yapıyoruz.

        else:
            print("Eksik yada fazla bilgi girişi yapıldı. Lütfen tekrar deneyiniz!")  # Yanlış bir değer girildiği zaman hata mesajı veriyoruz.

def listele():
    sayac=0
    while (sayac==0) :
        global Kafe
        Kafe = input("kafe gir:")  # kafe seçimini sorduk
        if Kafe in cafe:  # kullanıcıdan alınan kafe isminin, cafe listenin içinde olup olmadığını sorguluyoruz. cafe listesinin içinde "Kafe" varsa demek. Varsa sonraki adıma geçiyor.
            for C, K in menu[Kafe].items():  # burada menü ve fiyatlarını ekrana yazdıran kodu yazıyoruz. Yani menü dictionary de eklediğimiz kafe isimlerinin karşısındaki menüleri kullanıcının girdiği kafe ismine göre ekrana yazdırıyoruz.
                print(C, ":", K)
                sayac=1
        else:
            print("Lütfen bilgilerinizi kontrol ediniz!")

def secim():
    tekrar=0
    while tekrar==0:
        kahve = input("Kahve seçimi yapınız:")  # kahve seçimini sorduk.
        adet = int(input("Kaç adet istersiniz?")) #kaç adet olması gerektiğini kullanıcıya sorduk
        if kahve in menu[Kafe]: #kullanıcıdan aldığımız kahve değeri menu müzün içindeki değere karşılık geliyorsa anlamında kullanılan kod yapısı
            global toplam
            toplam = menu[Kafe][kahve] * adet  # burada menu dictionary sinin içinde eşleştirdiğimiz kafe menülerinden, kullacının girdiği kahvenin value değerini toplam adını verdiğimiz değişkene atıyoruz.
            global sepet
            sepet = {} # burada eklediğimiz ürünün ismini ve adedini listeleyeceğimiz dictionary değişkenimizi tanımlıyoruz
            sepet[kahve] = [adet] # sepetimize kahvenin ismine karşılık gelen adet sayısını ekliyoruz.
            global sonuc
            sonuc = toplam  # toplam adını verdiğimiz değişkeni sonuc adındaki yeni değişkene atıyoruz.
            girilsin = "evet"
            while girilsin == "evet":
                dongu = 1
                while dongu == 1:
                    ekle = input("Ekleme yapmak istiyor musunuz?") # Burada başka bir içecek sipariş edip etmeyeceğini kullanıcıya soruyoruz
                    if ekle == "evet" or ekle == "EVET" or ekle == "Evet": #cevap evet ise;
                        t = 1
                        while t == 1:
                            #kullanıcıya tekrardan yukarıdaki işlemleri yaptırıp sepete siparişi ekliyoruz.
                            menusec = input("Kahve seçimi yapınız:")
                            adet2 = int(input("Kaç adet istersiniz?"))
                            if menusec in menu[Kafe]:
                                sonuc = sonuc + (menu[Kafe][menusec] * adet2)
                                sepet[menusec] = [adet2]

                                girilsin="hayır"
                                tekrar=1
                                t=2

                            else:
                                print("Lütfen Bilgilerinizi Kontrol Ediniz!")

                    #hayır ise ekrana sepeti listeliyoruz ve ödenecek tutarı kullanıcıya gösteriyoruz.
                    elif ekle == "hayır" or ekle == "HAYIR" or ekle == "Hayır":
                        print("\n" + "         ALINANLAR")
                        for i, j in sepet.items():
                            print(i, j)
                        print("Hesap Tutarı:", sonuc , "TL")
                        dongu=2
                        girilsin="hayır"
                        tekrar=1

                    else:
                        print("Geçerli bir seçenek seçiniz. (evet/hayır)")
        else:
            print("Lütfen Bilgilerinizi Kontrol Ediniz!")

def odeme_yontemi():
    tekrar=0
    while tekrar==0:
        OdemeYontemi = input("Kredi karti mi ya da Nakit mi?")
        #kullanıcıya siparişi nasıl ödeyeceğini soruyoruz. Nakit ise;
        if OdemeYontemi == "nakit" or OdemeYontemi == "NAKİT" or OdemeYontemi == "Nakit":
            tutar = int(input("Lütfen Para Miktarı Giriniz:"))
            #kullanıcıdan vereceği para miktarını istiyoruz. Eğerki tutar sepet tutarına eşit yada büyük ise geri ödenecek tutarı  ekrana yazdırıyoruz.
            if tutar >= sonuc:
                ParaUstu = tutar - sonuc
                print("Para Ustunuz:", ParaUstu)
                print("Siparişiniz Alınmıştır...")
                print("Konum Bilgisi:", konum[Kafe])
                tekrar=1
            else: #kullanıcının vereceği paramiktarı sepet tutarından küçük ise hata veriyor
                print("Hatalı bir para miktarı girdiniz.")

        #kullınıcı kredi kartı seçerse, kart bilgilerini istiyoruz. Fakat kart bilgilerini alırken kullanıcı kart bilgisindeki numaraların uzunluğu kadar giriş yapmalı. Sonrasında sipariş tamamlanıyoru.
        elif OdemeYontemi == "kredi kartı" or OdemeYontemi == "KREDİ KARTI" or OdemeYontemi == "Kredi Kartı":
            KrediKartiBilgileri = open("kredikartı.txt", "a")
            kartno = input("Kart no:")
            if len(kartno) == 11:
                kartsonkul = input("Son kullanım tarihini giriniz:")
                if len(kartsonkul) == 4:
                    cvcno = input("CVC numarasını giriniz:")
                    if len(cvcno) == 3:
                        KrediKartiBilgileri.write(kartno + "\n" + kartsonkul + "\n" + cvcno)
                        KrediKartiBilgileri.close()
                        print("Siparişiniz Alınmıştır...")
                        print("Konum Bilgisi:", konum[Kafe])
                        tekrar=1
                    else:
                        print("geçerli bir CVC numarası giriniz.")
                else:
                    print("geçerli bir son kullanım tarihi giriniz giriniz.")
            else:
                print("geçerli bir kart numarası giriniz.")
        else:
            print("Geçerli bir ödeme yöntemi giriniz.")


try:
    cafelerAndMenu()
    para_konum_bilgisi()
    listele()
    secim()
    odeme_yontemi()
except:
    print("UPS! Birşeyler ters gitti...")