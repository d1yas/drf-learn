from rest_framework.throttling import BaseThrottle
import time

class CustomRateThrottle(BaseThrottle):
    """
    Custom throttling - har bir foydalanuvchi yoki IP-manzil uchun 1 daqiqada 5 ta so‘rov cheklov qo‘yadi.
    """
    rate = 5  # Maksimal ruxsat etilgan so‘rovlar soni
    cache = {}  # So‘rovlar vaqtini saqlash uchun xotira cache

    def allow_request(self, request, view):
        """
        So‘rovni ruxsat berish yoki yo‘qligini tekshiradi.
        """
        # Agar foydalanuvchi login qilgan bo‘lsa, uning ID sini ishlatamiz. Aks holda, IP-manzildan foydalanamiz.
        user_id = request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')

        # Foydalanuvchi uchun yangi ro‘yxat yaratamiz, agar u cache da bo‘lmasa.
        if user_id not in self.cache:
            self.cache[user_id] = []

        # Hozirgi vaqtni olish
        current_time = time.time()
        request_times = self.cache[user_id]

        # Eski so‘rovlarni o‘chirish (1 daqiqadan eski bo‘lgan so‘rovlar)
        while request_times and request_times[0] < current_time - 60:
            request_times.pop(0)

        # Yangi so‘rovni qo‘shish
        if len(request_times) < self.rate:
            request_times.append(current_time)
            return True  # Ruxsat beriladi
        return False  # So‘rov rad etiladi (429 Too Many Requests)

    def wait(self):
        """
        Foydalanuvchi qancha vaqt kutishi kerakligini qaytaradi.
        """
        return 60  
