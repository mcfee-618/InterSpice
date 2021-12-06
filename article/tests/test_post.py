from django.http import response
from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

class TestPost(TestCase):
    
    def test_post_detail(self):
        url = reverse("article:detail_post", args=[200])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        