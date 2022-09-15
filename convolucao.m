function imNew = convolucao(image,mask)
    [ny1,nx1]= size(image);
    [ny2,nx2]= size(mask);
    ny = ny1 - ny2 + 1;
    nx = nx1 - nx2 + 1;
        
    imNew = zeros(ny,nx);
    image = double(image);

    for y = 1:ny
        for x = 1:nx
            temp = mask .* image(y:y+ny2-1,x:x+nx2-1);
            imNew(y,x) = sum(temp(:));
        end
    end

    imNew = uint8(imNew);
end