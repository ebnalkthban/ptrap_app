import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/app_settings.dart';
import '../services/localization_service.dart';

class SettingsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final settings = Provider.of<AppSettings>(context);
    return Scaffold(
      appBar: AppBar(title: Text(context.tr('settings'))),
      body: ListView(
        children: [
          SwitchListTile(
            title: Text(context.tr('dark_mode')),
            value: settings.isDarkMode,
            onChanged: (_) => settings.toggleDarkMode(),
          ),
          Divider(),
          ListTile(title: Text(context.tr('language'))),
          ...LocalizationService.supportedLocales.map((locale) {
            return ListTile(
              title: Text(_getLanguageName(locale)),
              trailing: settings.languageCode == locale.languageCode ? Icon(Icons.check) : null,
              onTap: () => settings.setLanguage(locale.languageCode),
            );
          }),
        ],
      ),
    );
  }

  String _getLanguageName(Locale locale) {
    switch (locale.languageCode) {
      case 'ar': return 'العربية';
      case 'en': return 'English';
      case 'fr': return 'Français';
      case 'es': return 'Español';
      case 'de': return 'Deutsch';
      case 'ru': return 'Русский';
      case 'zh': return '中文';
      case 'fa': return 'فارسی';
      default: return locale.languageCode;
    }
  }
}