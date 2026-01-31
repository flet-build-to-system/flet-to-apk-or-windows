import flet as ft
import os
import subprocess

def main(page: ft.Page):
    # إعدادات الصفحة الرئيسية
    page.title = "Scrcpy Control Center"
    page.window_width = 800
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 30
    page.bgcolor = "#1a1a2e"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # وظائف تشغيل العمليات
    def run_command(cmd):
        try:
            # استخدام Popen لضمان عدم تجميد الواجهة عند تشغيل البرنامج
            subprocess.Popen(cmd, shell=True)
        except Exception as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {str(e)}"))
            page.snack_bar.open = True
            page.update()

    # دوال النقر للأزرار
    def scrcpy_click(e):
        run_command("scrcpy")

    def yacen_click(e):
        run_command("APP_Yacen_TV.bat")

    def geometry_click(e):
        run_command("APP_Geometry_Dash.bat")

    def facebook_click(e):
        run_command("APP_Facebook.bat")

    def anime_click(e):
        run_command("APP_Anime_Slayer.bat")
    
    def General_click(e):
        run_command("APP_General_TV.bat")

    def cmd_click(e):
        run_command("start cmd")

    # تنسيق الأزرار (ستايل موحد)
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=12),
        padding=20,
        color=ft.Colors.WHITE,
        bgcolor={
            ft.ControlState.DEFAULT: "#16213e",
            ft.ControlState.HOVERED: "#0f3460",
        },
    )

    # بناء الواجهة
    header = ft.Column(
        [
            ft.Icon(ft.Icons.SMARTPHONE_OUTLINED, size=50, color=ft.Colors.BLUE_400),
            ft.Text("جهاز التحكم بـ Scrcpy", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("اختر التطبيق أو الوضع الذي تريد تشغيله", color=ft.Colors.GREY_400),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # شبكة الأزرار (Grid-like Layout)
    buttons_grid = ft.Column([
        ft.Row([
            ft.ElevatedButton(
                "تشغيل العرض (Main)", 
                icon=ft.Icons.SCREEN_SHARE, 
                on_click=scrcpy_click, 
                style=button_style,
                expand=True
            ),
            ft.ElevatedButton(
                "Yacen TV", 
                icon=ft.Icons.TV, 
                on_click=yacen_click, 
                style=button_style,
                expand=True
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
        
        ft.Row([
            ft.ElevatedButton(
                "Geometry Dash", 
                icon=ft.Icons.GAMES, 
                on_click=geometry_click, 
                style=button_style,
                expand=True
            ),
            ft.ElevatedButton(
                "Facebook", 
                icon=ft.Icons.FACEBOOK, 
                on_click=facebook_click, 
                style=button_style,
                expand=True
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([
            ft.ElevatedButton(
                "Anime Slayer", 
                icon=ft.Icons.PLAY_CIRCLE_FILL, 
                on_click=anime_click, 
                style=button_style,
                expand=True
            ),

            ft.ElevatedButton(
                "General TV", 
                icon=ft.Icons.TV, 
                on_click=General_click, 
                style=button_style,
                expand=True
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([

            ft.ElevatedButton(
                "فتح CMD", 
                #icon=ft.icons.TERMINAL, 
                on_click=cmd_click, 
                style=button_style,
                expand=True
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
    ], spacing=20)

    # إضافة المحتويات للصفحة
    page.add(
        header,
        ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
        buttons_grid
    )
ft.run(main)

# تشغيل التطبيق
#if __name__ == "__main__":
#    ft.app(target=main)