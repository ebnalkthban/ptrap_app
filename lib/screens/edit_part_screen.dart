import 'package:flutter/material.dart';
import '../models/part.dart';
import '../services/local_db.dart';
import '../services/localization_service.dart';

class EditPartScreen extends StatefulWidget {
  final Part part;
  EditPartScreen({required this.part});

  @override
  State<EditPartScreen> createState() => _EditPartScreenState();
}

class _EditPartScreenState extends State<EditPartScreen> {
  late TextEditingController _nameController;
  late TextEditingController _quantityController;

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController(text: widget.part.name);
    _quantityController = TextEditingController(text: widget.part.quantity.toString());
  }

  Future<void> _update() async {
    widget.part.name = _nameController.text;
    widget.part.quantity = int.tryParse(_quantityController.text) ?? 0;
    await LocalDB.updatePart(widget.part);
    Navigator.pop(context);
  }

  Future<void> _delete() async {
    await LocalDB.deletePart(widget.part.id!);
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(context.tr('edit_part'))),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(controller: _nameController, decoration: InputDecoration(labelText: context.tr('name'))),
            SizedBox(height: 16),
            TextField(controller: _quantityController, decoration: InputDecoration(labelText: context.tr('quantity')), keyboardType: TextInputType.number),
            SizedBox(height: 32),
            ElevatedButton(onPressed: _update, child: Text(context.tr('save'))),
            SizedBox(height: 16),
            ElevatedButton(onPressed: _delete, child: Text(context.tr('delete')), style: ElevatedButton.styleFrom(backgroundColor: Colors.red)),
          ],
        ),
      ),
    );
  }
}