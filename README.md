# SOC-Beginner-Guide
دليل  للمبتدئين في مجال SOC
# 🛡️ دليل SOC للمبتدئين | SOC Beginner's Guide

![SOC Badge](https://img.shields.io/badge/SOC-Level1-blue)
![GitHub stars](https://img.shields.io/github/stars/yourname/SOC-Beginner-Guide)
![License](https://img.shields.io/github/license/yourname/SOC-Beginner-Guide)

## 📖 نظرة عامة
دليل شامل لبداية رحلة SOC Analyst، مبني على تجربتي الشخصية في كورس SOC Level 1 على TryHackMe.

## 🎯 الهدف من هذا الدليل
- مساعدة المبتدئين على فهم مجال SOC
- تقديم مسار تعليمي واضح
- مشاركة الخبرات والتحديات التي واجهتها

## 📚 المحتويات
1. [المتطلبات الأساسية](#المتطلبات-الأساسية)
2. [بداية الرحلة](#بداية-الرحلة)
3. [أدوات SOC](#أدوات-soc)
4. [سيناريوهات TryHackMe](#سيناريوهات-tryhackme)
5. [المسار المهني](#المسار-المهني)

## 🔧 المتطلبات الأساسية
### المعرفة التقنية:
- أساسيات الشبكات
- أساسيات لينكس
- مفاهيم الأمن السيبراني الأساسية

### الأدوات المطلوبة:
```bash
# قائمة بالأدوات المجانية
1. Wireshark - تحليل حركة الشبكة
2. Splunk Free - تحليل اللوجات
3. VirtualBox - الأجهزة الظاهرية
```

## 🚀 بداية الرحلة
### الخطوة الأولى: TryHackMe Pre-Security
```markdown
مسار مقترح:
1. Complete Beginner Path
2. Introduction to Cyber Security
3. SOC Level 1 (الذي أتممته)
```

## 📊 مثال: تحليل لوجات SSH
```python
#!/usr/bin/env python3
# محلل لوجات SSH البسيط

def analyze_ssh_logs(log_file):
    failed_attempts = 0
    suspicious_ips = []
    
    with open(log_file, 'r') as f:
        for line in f:
            if 'Failed password' in line:
                failed_attempts += 1
                # استخراج IP من اللوج
                ip = line.split('from ')[1].split(' ')[0]
                suspicious_ips.append(ip)
    
    return failed_attempts, suspicious_ips
```

## 🎮 سيناريوهات TryHackMe
| الغرفة | المستوى | المهارات المكتسبة |
|--------|---------|-------------------|
| Intro to Logs | مبتدئ | قراءة اللوجات الأساسية |
| Blue Team Fundamentals | متوسط | أساسيات الفريق الأزرق |
| SOC Level 1 | متقدم | مهارات SOC الأساسية |

## 🤝 المساهمة
نرحب بمساهماتكم! راجع [CONTRIBUTING.md](CONTRIBUTING.md) للتفاصيل.

## 📄 الرخصة
هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

---

⭐ **إذا أعجبك المشروع، لا تنسى إعطاء نجمه (Star)!**
