import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'services/app_settings.dart';
import 'services/localization_service.dart';
import 'services/local_db.dart';
import 'screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await LocalDB.init();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => AppSettings(),
      child: Consumer<AppSettings>(
        builder: (context, settings, _) {
          return MaterialApp(
            title: 'Phone Parts',
            theme: settings.isDarkMode ? ThemeData.dark() : ThemeData.light(),
            locale: Locale(settings.languageCode),
            localizationsDelegates: LocalizationService.localizationsDelegates,
            supportedLocales: LocalizationService.supportedLocales,
            home: HomeScreen(),
            debugShowCheckedModeBanner: false,
          );
        },
      ),
    );
  }
}
