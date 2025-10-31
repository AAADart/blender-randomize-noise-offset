# Randomize Noise Offset (Blender Add-on)

**Graph Editor → N → Modifiers → Randomize Noise Offset**  
Рандомізує параметр **Offset** у всіх **NOISE** F-Curve модифікаторах для активних екшенів вибраних об’єктів. Офсет задається в **секундах** (автоматично конвертується у кадри через FPS).

![Panel](assets/screenshot_panel.png)

## Можливості
- Працює по **вибраних об’єктах** (якщо їх немає — по активному).
- **Seed** для відтворюваності.
- **Offset Min/Max (s)** — діапазон у секундах, конвертується у кадри.

## Вимоги
- Blender **4.0+** (тестовано на 4.5)

## Встановлення
1. Завантаж ZIP реліз або зробіть ZIP з папки `addon/randomize_noise_offset`.
2. У Blender: **Edit → Preferences → Add-ons → Install...** → оберіть ZIP → **Install**.
3. Активуйте аддон (галочка).
4. Відкрийте **Graph Editor**, натисніть **N** → вкладка **Modifiers** → секція **Randomize Noise Offset**.

## Використання
1. Виділіть об’єкти з анімацією (або залиште активний об’єкт з Action).
2. Вкажіть **Seed**, **Offset Min/Max (s)**.
3. Натисніть **Randomize Noise Offset** — усі NOISE модифікатори отримають випадковий офсет.

## Чому аддон?
У Blender немає стандартної кнопки/оператора, який масово рандомізує Offset у NOISE модифікаторах. Без аддона це робиться лише вручну.

## Доробки (ідеї)
- Опція працювати **за виділеними F-curves** у Graph Editor.
- Перемикач «працювати в **кадрах** замість секунд».
- Додати фільтр за іменем Action / каналами.

## Розробка
- Код — в `addon/randomize_noise_offset/__init__.py`.
- Стиль: PEP8, префікси класів `RNO_`/`GRAPH_`.
- PR-и та issue — вітаються!

## Ліцензія
MIT — див. [LICENSE](LICENSE).
