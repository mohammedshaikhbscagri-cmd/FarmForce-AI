import 'package:flutter/material.dart';

class RatingWidget extends StatelessWidget {
  final double rating;
  final int maxStars;
  final double size;

  const RatingWidget({super.key, required this.rating, this.maxStars = 5, this.size = 20});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        ...List.generate(maxStars, (i) => Icon(
          i < rating.floor() ? Icons.star : i < rating ? Icons.star_half : Icons.star_border,
          color: Colors.amber,
          size: size,
        )),
        const SizedBox(width: 4),
        Text(rating.toStringAsFixed(1), style: TextStyle(fontSize: size * 0.8, fontWeight: FontWeight.bold)),
      ],
    );
  }
}
