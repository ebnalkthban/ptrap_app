import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/app_settings.dart';
import 'inventory_screen.dart';
import 'settings_screen.dart';
import '../services/localization_service.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer<AppSettings>(
      builder: (context, settings, _) {
        return Scaffold(
          appBar: AppBar(title: Text(context.tr('app_title'))),
          body: Row(
            children: [
              NavigationRail(
                selectedIndex: 0,
                onDestinationSelected: (index) {},
                labelType: NavigationRailLabelType.selected,
                destinations: [
                  NavigationRailDestination(icon: Icon(Icons.inventory), label: Text(context.tr('inventory'))),
                  NavigationRailDestination(icon: Icon(Icons.settings), label: Text(context.tr('settings'))),
                ],
              ),
              Expanded(child: InventoryScreen()),
            ],
          ),
        );
      },
    );
  }
}