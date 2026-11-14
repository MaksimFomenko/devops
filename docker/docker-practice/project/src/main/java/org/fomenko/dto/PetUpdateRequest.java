package org.fomenko.dto;

public record PetUpdateRequest(String name, int age, String type) {
}