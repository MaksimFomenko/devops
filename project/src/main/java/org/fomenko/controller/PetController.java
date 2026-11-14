package org.fomenko.controller;

import org.fomenko.dto.PetRequest;
import org.fomenko.dto.PetUpdateRequest;
import org.fomenko.model.Pet;
import org.fomenko.model.User;
import org.fomenko.service.pet_service.PetService;
import org.fomenko.service.user_service.UserService;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/pets")
public class PetController {
    private final PetService petService;
    private final UserService userService;

    public PetController(PetService petService, UserService userService) {
        this.petService = petService;
        this.userService = userService;
    }

    @GetMapping
    public List<Pet> getAllPets() {
        return petService.getAllPets();
    }

    @GetMapping("/{id}")
    public Pet getPetById(@PathVariable int id) {
        return petService.getPetById(id);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public void createPet(@RequestBody PetRequest request) {
        User owner = userService.getUserById(request.userId())
                .orElseThrow(() -> new IllegalArgumentException("User with ID " + request.userId() + " does not exist"));
        petService.addPet(new Pet(request.name(), request.age(), request.type(), owner));
    }

    @PutMapping("/{id}")
    public Pet updatePet(@PathVariable int id, @RequestBody PetUpdateRequest request) {
        return petService.updatePet(id, request.name(), request.age(), request.type());
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deletePet(@PathVariable int id) {
        petService.deletePetById(id);
    }
}