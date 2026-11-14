package org.fomenko.dto;

public record PetRequest(String name, int age, String type, Integer userId) {
}