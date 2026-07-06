import 'package:flutter/material.dart';
import 'package:mobile_scanner/mobile_scanner.dart';
import '../services/local_db.dart';
import '../models/part.dart';
import '../services/localization_service.dart';

class AddPartScreen extends StatefulWidget {
  @override
  State<AddPartScreen> createState() => _AddPartScreenState();
}

class _AddPartScreenState extends State<AddPartScreen> {
  final _nameController = TextEditingController();
  final _quantityController = TextEditingController();
  String? _barcode;

  Future<void> _scanBarcode() async {
    final result = await Navigator.push(context, MaterialPageRoute(builder: (_) => ScanScreen()));
    if (result != null) setState(() => _barcode = result);
  }

  Future<void> _save() async {
    if (_nameController.text.isEmpty) return;
    final part = Part(
      name: _nameController.text,
      barcode: _barcode,
      quantity: int.tryParse(_quantityController.text) ?? 0,
    );
    await LocalDB.insertPart(part);
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(context.tr('add_part'))),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(controller: _nameController, decoration: InputDecoration(labelText: context.tr('name'))),
            SizedBox(height: 16),
            Row(
              children: [
                Expanded(child: TextField(controller: _quantityController, decoration: InputDecoration(labelText: context.tr('quantity')), keyboardType: TextInputType.number)),
                IconButton(icon: Icon(Icons.qr_code_scanner), onPressed: _scanBarcode),
              ],
            ),
            if (_barcode != null) Text('${context.tr('barcode')}: $_barcode'),
            SizedBox(height: 32),
            ElevatedButton(onPressed: _save, child: Text(context.tr('save'))),
          ],
        ),
      ),
    );
  }
}