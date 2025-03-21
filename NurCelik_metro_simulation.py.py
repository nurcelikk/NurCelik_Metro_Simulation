from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """
    graph={
        'AŞTİ':['KIZILAY'],
        'KIZILAY':['SIHHIYE'],
        'SIHHIYE':['GAR'],
        'GAR':[],
        'KIZILAY':['ULUS'],
        'ULUS':['DEMETEVLER'],
        'DEMETEVLER':['OSB'],
        'OSB':[],
        'BATIKENT':['DEMETEVLER'],
        'DEMETEVLER':['GAR'],
        'GAR':['KEÇİÖREN'],
        'KEÇİÖREN':[]
    }    
    
        
    def bfs(graph,baslangic_id):
        visited=set()
        queue=[baslangic_id]

        while queue:
            node=queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node,end=' ') 
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    print("Genislik Oncelikli Arama Sonucu:")
    bfs(graph,'KIZILAY')
                                       


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
       
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]


start=(0,0)
goal= (4,4)

import heapq
def a_star(start,goal,grid):
 directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

 def heuristic(a, b):
    """Manhattan mesafesini hesaplar (sezgisel fonksiyon)"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

 def is_valid_cell(cell):
    """Hücrenin geçerli olup olmadığını kontrol eder"""
    row, col = cell

    # Izgaranın içinde mi?
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
      return False

    # Engel değil mi?
    if grid[row][col] == 1:
      return False

    return True
 def reconstruct_path(came_from, current):
    """Bulunan yolu başlangıçtan hedefe doğru yeniden oluşturur"""
    path = []
    while current in came_from:
      path.append(current)
      current = came_from[current]
    return path[::-1]  # Yolu tersine çevir (başlangıçtan hedefe)

 frontier = []  # Frontier - keşfedilecek düğümleri tutan öncelikli kuyruk
 came_from = {
        'AŞTİ':['KIZILAY'],
        'KIZILAY':['SIHHIYE'],
        'SIHHIYE':['GAR'],               # Her düğüme hangi düğümden gelindiğini tutar
        'GAR':[],
        'KIZILAY':['ULUS'],
        'ULUS':['DEMETEVLER'],
        'DEMETEVLER':['OSB'],
        'OSB':[],
        'BATIKENT':['DEMETEVLER'],
        'DEMETEVLER':['GAR'],
        'GAR':['KEÇİÖREN'],
        'KEÇİÖREN':[]
    }  
 g_score = {start: 0}  # Başlangıçtan düğüme olan maliyet (g(n))
 f_score = {start: heuristic(start,goal)}  # Toplam tahmin (f(n) = g(n) + h(n))

  # (f(n), g(n), düğüm) olarak ekle, f(n) değerine göre sıralanır
 heapq.heappush(frontier, (heuristic(start,goal), 0, start))

 while frontier:
    # En düşük f(n) değerine sahip düğümü çıkar
  _, current_g, current = heapq.heappop(frontier)

    # Hedef düğüme ulaşıldı mı?
  if current == goal:
    return reconstruct_path(came_from, current)

    # Komşuları kontrol et
    for direction in directions:
      neighbor = (current[0] + direction[0], current[1] + direction[1])

      # Komşu hücre geçerli mi?
      if not is_valid_cell(neighbor):
        continue  # Geçersiz hücre, bir sonraki komşuya geç

      # Komşuya giden yeni yol maliyeti (g(n))
      tentative_g = current_g + 5  # Her adımın maliyeti bu örnekte 5 (NOT: projede ve asagidaki ornek)

      # Daha iyi bir yol bulunduysa güncelle
      if neighbor not in g_score or tentative_g < g_score[neighbor]:
        came_from[neighbor] = current  # Yolu güncelle
        g_score[neighbor] = tentative_g  # g(n) değerini güncelle
        f_score[neighbor] = tentative_g + heuristic(neighbor, goal)  # f(n) değerini güncelle
        heapq.heappush(frontier, (f_score[neighbor], tentative_g, neighbor))  # Komşuyu öncelikli kuyruğa ekle

  return None  # Çözüm bulunamadı
        



        

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 