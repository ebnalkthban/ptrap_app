import 'package:flutter/material.dart';
import '../services/local_db.dart';
import '../models/part.dart';
import 'add_part_screen.dart';
import 'edit_part_screen.dart';
import '../services/localization_service.dart';

class InventoryScreen extends StatefulWidget {
  @override
  State<InventoryScreen> createState() => _InventoryScreenState();
}

class _InventoryScreenState extends State<InventoryScreen> {
  List<Part> _parts = [];
  String _searchQuery = '';

  @override
  void initState() {
    super.initState();
    _loadParts();
  }

  Future<void> _loadParts() async {
    final parts = await LocalDB.getAllParts();
    setState(() => _parts = parts);
  }

  Future<void> _search(String query) async {
    _searchQuery = query;
    if (query.isEmpty) {
      await _loadParts();
    } else {
      final results = await LocalDB.searchParts(query);
      setState(() => _parts = results);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              decoration: InputDecoration(hintText: context.tr('search'), prefixIcon: Icon(Icons.search)),
              onChanged: _search,
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: _parts.length,
              itemBuilder: (context, index) {
                final part = _parts[index];
                return ListTile(
                  title: Text(part.name),
                  subtitle: Text('${context.tr('quantity')}: ${part.quantity} ${part.quantity < 5 ? "⚠️" : ""}'),
                  trailing: part.quantity < 5 ? Icon(Icons.warning, color: Colors.orange) : null,
                  onTap: () async {
                    await Navigator.push(context, MaterialPageRoute(builder: (_) => EditPartScreen(part: part)));
                    _loadParts();
                  },
                );
              },
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () async {
          await Navigator.push(context, MaterialPageRoute(builder: (_) => AddPartScreen()));
          _loadParts();
        },
      ),
    );
  }
}