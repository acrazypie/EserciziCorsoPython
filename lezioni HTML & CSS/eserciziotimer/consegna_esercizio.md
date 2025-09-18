# Esercizio — **Pomodoro Lite** (timer lavoro + pausa)

## Obiettivi didattici
- Usare `setInterval` / `clearInterval` per creare un timer.
- Gestire **stato** applicativo (`work` / `break`, tempo totale, tempo rimanente, running).
- Manipolare il **DOM** (testi, classi, barra di progresso).
- Gestire **eventi**: `Start`, `Pausa`, `Reset`, `Skip`.
- **No** storage, **no** librerie: solo HTML/CSS/JS vanilla.

---

## Requisiti & Setup
- Crea un progetto con questi file:
  ```
  /pomodoro-lite
    index.html
    style.css
    main.js
  ```
- Apri con Live Server (o semplicemente il file HTML).

---

## Consegna
Realizza un timer Pomodoro con:
1. **Impostazioni**: due input numerici per minuti di **Lavoro** e **Pausa** (default 25 e 5).
2. **Display**:  
   - Stato corrente: “Lavoro” o “Pausa”.  
   - Timer in formato `MM:SS`.  
   - **Progress bar** che avanza con il passare del tempo.
3. **Controlli**:  
   - `Start`: avvia il conto alla rovescia.  
   - `Pausa`: mette in pausa.  
   - `Reset`: torna a Lavoro con i valori correnti degli input.  
   - `Skip`: salta alla fase successiva (da Lavoro → Pausa o viceversa).
4. **Comportamento**:  
   - Un solo intervallo attivo alla volta (evita doppi `setInterval`).  
   - Quando finisce **Lavoro**, parte **Pausa** automaticamente.  
   - Quando finisce **Pausa**, il timer si ferma e si prepara a **Lavoro**.  
   - Aggiorna sempre UI e pulsanti (abilita/disabilita) in modo coerente.

**Vincoli**
- Niente `localStorage`.  
- Niente librerie esterne.  
- Mantieni la logica in funzioni piccole: es. `tick()`, `updateUI()`, `setupPhase(mode)`.

---

## Suggerimenti di implementazione
- Mantieni uno stato minimo:
  ```js
  let mode = 'work';      // 'work' | 'break'
  let total = 25 * 60;    // secondi totali della fase
  let remaining = total;  // secondi rimanenti
  let running = false;
  let tickId = null;      // id restituito da setInterval
  ```
- Crea una utility per formattare `MM:SS`:
  ```js
  const mmss = s => `${String(Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`;
  ```
- Progress bar: percentuale = `1 - remaining / total`.
- Disabilita/abilita i pulsanti in base a `running`.

---

## Criteri di valutazione
- **Funzionalità**: timer corretto, passaggi work/break (40%)
- **Stato & UI**: pulsanti e barra coerenti (30%)
- **Qualità codice**: funzioni piccole, nomi chiari, niente duplicazioni (20%)
- **Stile**: HTML/CSS ordinati, accessibilità base (10%)

---

## Esempio minimo di `setInterval`
> Esegui una funzione ogni secondo e fermati dopo 5 tick.
```js
let n = 0;

// Esegue la funzione ogni 1000 ms (1 secondo)
const id = setInterval(() => {
  n++;
  console.log('Tick:', n);

  if (n === 5) {
    clearInterval(id); // FERMA l'intervallo
    console.log('Stop.');
  }
}, 1000);
```

---

## Bonus (facoltativi)
- **Beep** al cambio fase (Web Audio API semplice).
- **Tema scuro** con toggle.
- Pulsanti **+1 min / -1 min** utilizzabili in pausa.

---

## Consegna finale
- Carica la cartella (o link Git) con `index.html`, `style.css`, `main.js`.
- Aggiungi un breve `README.md` con note su scelte implementative.
