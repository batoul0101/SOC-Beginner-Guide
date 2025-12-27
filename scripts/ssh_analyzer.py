
محلل لوجات SSH - SOC-Beginner-Guide
أداة لاكتشاف هجمات Brute Force على SSH
---------------------------------------------------------------------------------
import re
import sys
from collections import Counter
from datetime import datetime

def analyze_ssh_logs(log_file, threshold=10):
    """
    تحليل ملف لوجات SSH
    
    Args:
        log_file (str): مسار ملف اللوجات
        threshold (int): عتبة الشك (عدد المحاولات)
    
    Returns:
        dict: نتائج التحليل
    """
    
    print(f"[*] بدء تحليل: {log_file}")
    print(f"[*] الوقت: {datetime.now()}")
    print(f"[*] عتبة الشك: {threshold} محاولة")
    print("=" * 50)
    
    results = {
        'total_lines': 0,
        'failed_attempts': 0,
        'successful_logins': 0,
        'suspicious_ips': {},
        'timeline': []
    }
    
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                results['total_lines'] += 1
                
                # تحليل كل سطر
                if 'Failed password' in line:
                    results['failed_attempts'] += 1
                    
                    # استخراج IP
                    ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        
                        # تحديث العدادات
                        if ip in results['suspicious_ips']:
                            results['suspicious_ips'][ip] += 1
                        else:
                            results['suspicious_ips'][ip] = 1
                        
                        # استخراج الوقت
                        time_match = re.search(r'(\w+ \d+ \d+:\d+:\d+)', line)
                        if time_match:
                            results['timeline'].append({
                                'time': time_match.group(1),
                                'ip': ip,
                                'type': 'failed'
                            })
                
                elif 'Accepted password' in line:
                    results['successful_logins'] += 1
        
        # توليد التقرير
        print(f"[+] تم تحليل {results['total_lines']} سطر")
        print(f"[+] المحاولات الفاشلة: {results['failed_attempts']}")
        print(f"[+] الدخول الناجح: {results['successful_logins']}")
        
        # عرض IPs المشبوهة
        if results['suspicious_ips']:
            print(f"\n[!] IPs المشبوهة (أكثر من {threshold} محاولة):")
            suspicious_count = 0
            
            for ip, count in sorted(results['suspicious_ips'].items(), 
                                   key=lambda x: x[1], reverse=True):
                if count >= threshold:
                    print(f"    {ip}: {count} محاولة")
                    suspicious_count += 1
            
            if suspicious_count == 0:
                print("    لا توجد IPs مشبوهة")
        
        return results
    
    except FileNotFoundError:
        print(f"[-] خطأ: الملف {log_file} غير موجود")
        return None
    except Exception as e:
        print(f"[-] خطأ غير متوقع: {e}")
        return None

def generate_report(results, output_file=None):
    """توليد تقرير مفصل"""
    if not results:
        return
    
    report = []
    report.append("=" * 60)
    report.append("تقرير تحليل هجمات SSH - SOC Beginner Guide")
    report.append("=" * 60)
    report.append(f"تاريخ التقرير: {datetime.now()}")
    report.append(f"إجمالي الأسطر المحللة: {results['total_lines']}")
    report.append(f"المحاولات الفاشلة: {results['failed_attempts']}")
    report.append(f"المحاولات الناجحة: {results['successful_logins']}")
    
    if results['suspicious_ips']:
        report.append("\n📊 إحصائيات IPs المشبوهة:")
        for ip, count in sorted(results['suspicious_ips'].items(), 
                               key=lambda x: x[1], reverse=True)[:10]:
            report.append(f"  {ip}: {count} محاولة")
    
    report.append("\n💡 التوصيات:")
    if results['failed_attempts'] > 50:
        report.append("1. تفعيل fail2ban على السيرفر")
    if len(results['suspicious_ips']) > 5:
        report.append("2. مراجعة قواعد الجدار الناري")
    
    report.append("\n" + "=" * 60)
    
    report_text = "\n".join(report)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"[+] تم حفظ التقرير في: {output_file}")
    else:
        print(report_text)

def main():
    """الدالة الرئيسية"""
    print("=" * 60)
    print("محلل لوجات SSH - SOC Beginner Guide")
    print("=" * 60)
    
    # إعداد المدخلات
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = input("أدخل مسار ملف اللوجات: ").strip()
    
    threshold = 10  # عتبة الشك الافتراضية
    
    # التحليل
    results = analyze_ssh_logs(log_file, threshold)
    
    if results:
        # توليد التقرير
        output_file = f"ssh_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        generate_report(results, output_file)
        
        print(f"\n✅ تم الانتهاء من التحليل بنجاح!")
        print(f"📁 يمكنك العثور على التقرير في: {output_file}")

if __name__ == "__main__":
    main()
