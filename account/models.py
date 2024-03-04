# usatlarni ko'rish
# har bir orderni ko'rib turish
# kassa
# payment
# Order
#
#
# Models
# User
# employee
# Cassa
# Order
# Payment
# Report
#
#
# Fields
#
# User:
# 1username
# 2phone_number
# 3.password
#
#
# Emplayee: =              Xodim:
# 1.user OneToOneField =   1.foydalanuvchi OneToOneField
# 2. profession = #        2. kasb
# 3. wages = №             3. ish haqi
# 4. age = №               4. yosh
# 5. address = №           5. manzil
# 6. experience = №        6. tajriba
# 7. work_time = №         7. ish_vaqti
# 8. rating = №            8. reyting
# 9. garaj OnaToOne = #    9. garaj OnaToOne
#
#
#
# Cassa:
# summa
#
#
# Order:   =              # Buyurtma:
# qr_code   =             # qr_kod
# owner_name   =          # egasi_ismi
# owner_phone number   =  # egasining_telefon raqami
# is_delivery = bool   =  # yetkazib berilmoqda = bool
# address =   =           # manzil =
# car_name   =            # avtomobil_nomi
# car_number   =          # avtomobil_raqami
# is_active   =           # faol
# master employee   =     # bosh xodim
# problem   =             # muammo
# service_cost   =        # xizmat_narxi
# start_day   =           # boshlanish_kuni
# start_time   =          # Boshlanish vaqti
#
#
#
# payment:                 to'lov:
# order                   # buyurtma
# code                    # kod
# payment                 # to'lov
# date                    # sana
# payment_type=choices    # to'lov_turi=tanlovlar
# admin = FK employee     # admin = FK xodimi
# qr_code                 # qr_kod
#
#
# Report
# start_date
# end_date
# income
# spend
#
#
# garaj
# number