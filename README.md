# BSD Workshop Skills — ชุดทดลองแจกผ่าน GitHub

สถานะ PUBLISHED SKILL / BSD ONLINE RUNTIME NOT TESTED

ชุดนี้นำ `frontend-ui-quality` จากแพ็ก Skills v0.3 ที่ใช้ใน Local IDE มาเตรียมแจกสำหรับ BSD Online AI เนื้อหา Skill คัดลอกเดิมทุกไบต์ พร้อมตาราง Provenance และ license ที่อ้างอิง เลือกหนึ่ง Skill เพื่อทดลองปรับ UI ของ MVP ที่มีอยู่แล้ว

## รูปแบบการใช้งานที่ออกแบบ

1. ครูเผยแพร่เนื้อหาโฟลเดอร์นี้ใน repository สำหรับแจก Skills แล้วระบุ commit ของชุดที่ใช้สอน
2. แจก URL แบบ Raw ที่ชี้ commit นั้น พร้อม prompt ติดตั้งจาก `PROMPTS.md`
3. BSD AI โหลดเนื้อหา สร้าง `workshop-ui.SKILL.md` ในโปรเจกต์ทดสอบ และรายงานหลักฐานที่มี
4. ครูตรวจเนื้อหาไฟล์หลัง reload และเทียบ hash ด้วยเครื่องมือที่ครูใช้ได้
5. ผู้เรียนใช้ prompt ปรับ MVP โดยเรียกไฟล์นั้นชัดเจน พร้อม Wish หนึ่งข้อและเกณฑ์ผ่าน
6. ตรวจ diff, Preview, พฤติกรรมเดิม และไฟล์ที่บันทึก ก่อนส่งต่อ SELL

เรียกขั้นตอนนี้ว่า **โหลดคำแนะนำจากไฟล์โปรเจกต์ด้วย prompt** การยืนยัน Native Skill discovery ต้องมีการทดสอบและ trace แยกต่างหาก

## รายการไฟล์แจก

- `skills/frontend-ui-quality/SKILL.md` — Skill เดิม 5,238 bytes
- `LICENSES/` — license จากแพ็กเดิมสำหรับแหล่งที่ Skill อ้างอิง
- `manifest.json` — version, hash, รายการอ้างอิง และสถานะทดสอบ
- `PROMPTS.md` — prompt เตรียมไฟล์และ prompt ปรับ MVP
- `TEST_PROTOCOL.md` — แผนตรวจ fetch, file roundtrip, context และการใช้งานจริง

Skill เดิมอ้างถึง `testing-and-verification` และ “standard core report” ซึ่งชุดทดลองหนึ่ง Skill นี้ยังไม่ได้แนบ Prompt จึงกำหนดการรายงานผลและรายการที่ต้องให้ครู/ผู้เรียนตรวจไว้ชัดเจน การทดลองจะบันทึกว่ามี Skill อื่นถูกอ่านหรือถูกระบบเติมเข้ามาหรือไม่

## การเข้าถึง GitHub

ชุดนี้เผยแพร่เฉพาะไฟล์สำหรับแจกผู้เรียนใน `Anurog1112/bsd-workshop-skills` การเข้าถึง Raw URL จาก BSD AI ต้องตรวจผ่านเส้นทางที่ AI ใช้จริงด้วย

Raw URL ของ Skill รุ่นทดลองที่ตรวจการเข้าถึงแล้ว

```text
https://raw.githubusercontent.com/Anurog1112/bsd-workshop-skills/264670596977af70a314572def0bcf49de842ec6/skills/frontend-ui-quality/SKILL.md
```

Skill ใช้ commit ที่ระบุใน manifest ส่วน README และ prompt อาจมี commit ใหม่กว่าได้ เก็บ URL และ commit ของ Skill ที่ใช้จริงในบันทึกการทดลอง หากเปลี่ยน Skill ให้เปลี่ยน commit และตรวจ prompt กับ hash ใหม่

## ทางสำรองที่ต้องทดลอง

- โหลด URL ไม่ได้ แต่โมเดลอ่าน prompt ได้ — ครูแจกข้อความ Skill ทั้งไฟล์ให้คัดลอก แล้วใช้เป็น Explicit Guidance
- โหลดได้ แต่สร้าง `.md` ไม่สำเร็จ — บันทึกข้อผิดพลาดจริง ทดลอง Explicit Guidance ต่อโดยระบุว่ายังไม่ผ่าน file roundtrip
- `.md` อยู่ในโปรเจกต์ แต่ยังพิสูจน์การอ่านไม่ได้ — ตรวจ input assembly/tool trace หรือจัดสถานะ AI file reading เป็น NOT TESTED
- AI ทำการเปลี่ยนแปลงผิดขอบเขต — เก็บหลักฐาน แล้วคืน baseline ก่อนรอบเปรียบเทียบ

## หลักฐานปัจจุบัน

SOURCE-VERIFIED เฉพาะเนื้อหาและการคัดลอก Skill จากแพ็กเดิม รวมถึงรายการอ้างอิงใน Skill

NOT TESTED สำหรับการโหลด Raw URL โดย BSD AI, สร้างและเปิด `.md` กลับบน BSD, การใช้กฎกับ MVP, Native discovery และเวลาที่ผู้เรียนใช้จริง
